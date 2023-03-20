from flask import Flask, request, render_template
import os
from serveranswer_query import answer_question
from servercontext import bert_abstract
from transformers import BertTokenizer
import pickle
#import pika

app = Flask(__name__)
tokenizer = BertTokenizer.from_pretrained(
        'bert-large-uncased-whole-word-masking-finetuned-squad')

with open('BERT_DL_model.pkl', 'rb') as file:
        BERT_DL_Model = pickle.load(file)

@app.route("/")
def main():
    return render_template("question.html")

@app.route('/answer', methods=["POST"])
def answer():
    question = request.form.get("question")
    answer = answer_question(question, bert_abstract, BERT_DL_Model, tokenizer)
    return render_template("answer.html", question=question, answer=answer)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '3000'))