import pickle
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained(
        'bert-large-uncased-whole-word-masking-finetuned-squad')

with open('BERT_DL_model.pkl', 'rb') as file:
        BERT_DL_Model = pickle.load(file)

def answer_question(question):
    return "__Got the question: %s" % question