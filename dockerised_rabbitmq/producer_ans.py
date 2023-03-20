import pika
import json

params = pika.URLParameters(
    'amqps://ihmjanpu:4XqHoydYlSJeU-tvf0M_HjDgN98uqG17@puffin.rmq2.cloudamqp.com/ihmjanpu')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='answer', durable=True)


def publish_answer(answer):
    channel.basic_publish(exchange='', routing_key='answer',
                          body=json.dumps(answer), properties=pika.BasicProperties(delivery_mode=2))
