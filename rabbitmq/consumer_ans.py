import pika
import json
from decouple import config

params = pika.URLParameters(config('RABBIT_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()


def callback(ch, method, properties, body):
    answer = json.loads(body)
    print(f'Received answer: {answer} \n')
    with open('answer.txt', 'w') as f:
        f.write(answer)


channel.basic_consume(
    queue='answer', on_message_callback=callback, auto_ack=True)

print('Started consuming from answer queue')
channel.start_consuming()
channel.close()
