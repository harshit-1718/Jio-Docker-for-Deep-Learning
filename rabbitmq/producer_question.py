import pika
import json
from decouple import config

params = pika.URLParameters(config('RABBIT_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main', durable=True)


def publish_question(question):
    channel.basic_publish(exchange='', routing_key='main',
                          body=json.dumps(question), properties=pika.BasicProperties(delivery_mode=2))
