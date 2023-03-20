import json
import pika

def callback(ch, method, properties, body):
    print(" Received %r" % json.loads(body))
    obj = json.loads(body)
    # print(obj);
    print(obj["payload"]["ans"])
    ch.basic_ack(delivery_tag=method.delivery_tag)
    

def pika_consumer():
    print("Enterred pika_consumer for answer_queue")
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
        print("Connected to RabbitMQ service")
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
    while(True):
        consumer_channel = connection.channel()
        consumer_channel.basic_qos(prefetch_count=1)
        consumer_channel.basic_consume(
            queue='answer_queue', on_message_callback=callback,auto_ack=True)
        # print('tag', tag)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        try:
            consumer_channel.start_consuming()
            print("Consumption successful.")
        except Exception as e:
            print("Consumption failed. --",e)
    # connection.close()

def pika_producer(answer):
    print("Received answer in the producer ", answer)
    print(answer)

pika_consumer()
