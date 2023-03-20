import pika
import json
import pickle
from transformers import BertTokenizer
from answer_query import answer_question
from context import bert_abstract

tokenizer = BertTokenizer.from_pretrained(
        'bert-large-uncased-whole-word-masking-finetuned-squad')

with open('BERT_DL_model.pkl', 'rb') as file:
        BERT_DL_Model = pickle.load(file)


def callback(ch, method, properties, body):
    print('Gone into callback')
    # print(" Received %r" % json.loads(body))
    obj = json.loads(body)
    print('Printing Question' , obj)
    # print(" Done")
    answer = answer_question(obj["payload"]["question"], bert_abstract, BERT_DL_Model, tokenizer)
    
    print(answer)
    print(type(answer))
    pika_producer(answer, obj["payload"]["id"])
    ch.basic_ack(delivery_tag=method.delivery_tag)

def pika_producer(answer, id):
    
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
    
    #create a json object
    json_object =  {
        "payload": {
            "id": id,
            "ans" : answer
          }
        }
    
    channel = connection.channel()
    channel.queue_declare(queue='answer_queue', durable=True)
    channel.basic_publish(exchange='', routing_key='answer_queue', body=json.dumps(json_object))
    print(" [x] Sent 'Json Object'")
    #connection.close()

def pika_consumer():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
    while(True):
        consumer_channel = connection.channel()
        consumer_channel.basic_qos(prefetch_count=1)
        consumer_channel.basic_consume(
            queue='task_queue', on_message_callback=callback,auto_ack=False)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        try:
            consumer_channel.start_consuming()
            print("Consumption successful.")
        except Exception as e:
            print("Consumption failed. --",e)

if __name__=="__main__":
    pika_consumer()