from flask import Flask, request, render_template
import os
from rabbitmq.producer_question import publish_question
import os.path

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("question.html")


@app.route('/answer', methods=["POST"])
def answer():

    question = request.form.get("question")
    publish_question(question)
    while(not os.path.exists('rabbitmq/answer.txt')):
        continue
    with open('rabbitmq/answer.txt', 'r') as f:
        answer = f.read()
    os.remove("rabbitmq/answer.txt")
    return render_template("answer.html", question=question, answer=answer)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', '3000'))
