import pika
import json
from decouple import config

params = pika.URLParameters(config('RABBIT_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='answer', durable=True)


def publish_answer(answer):
    channel.basic_publish(exchange='', routing_key='answer',
                          body=json.dumps(answer), properties=pika.BasicProperties(delivery_mode=2))
