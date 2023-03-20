from flask import Flask
import pika
import uuid
import json


app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'


@app.route('/create-job/<question>')
def add(question):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")

    json_obj =  {
        "payload": {
            "id": str(uuid.uuid4()),
            "question" : question
          }
        }
    print(question);
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=json.dumps(json_obj),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    connection.close()
    # pika_consumer()
    return 'DONE'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    