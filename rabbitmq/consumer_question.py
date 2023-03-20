import pika
import json
from answer_query import answer_question
from context import bert_abstract
from transformers import BertTokenizer
import pickle
from decouple import config

from producer_ans import publish_answer

tokenizer = BertTokenizer.from_pretrained(
    'bert-large-uncased-whole-word-masking-finetuned-squad')
with open('BERT_DL_model.pkl', 'rb') as file:
    BERT_DL_Model = pickle.load(file)

params = pika.URLParameters(config('RABBIT_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()


def callback(ch, method, properties, body):
    question = json.loads(body)
    print(f'Received question: {question} \n')
    answer = answer_question(question, bert_abstract, tokenizer, BERT_DL_Model)
    publish_answer(answer)


channel.basic_consume(
    queue='main', on_message_callback=callback, auto_ack=True)

print('Started consuming from question queue')

channel.start_consuming()

channel.close()
connection.close()
