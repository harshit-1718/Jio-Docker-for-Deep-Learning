import pika
import json

params = pika.URLParameters(
    'amqps://ihmjanpu:4XqHoydYlSJeU-tvf0M_HjDgN98uqG17@puffin.rmq2.cloudamqp.com/ihmjanpu')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main', durable=True)


def publish_question(question):
    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(question), properties=pika.BasicProperties(delivery_mode=2))
