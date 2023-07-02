import random
import json
import pickle
import os
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model

nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
# file_path = os.path.join(os.path.dirname(__file__), 'words.pkl')
file_path = 'static/words.pkl'
words = pickle.load(open(file_path, 'rb'))
# file_path2 = os.path.join(os.path.dirname(__file__), 'classes.pkl')
file_path2 = 'static/classes.pkl'
classes = pickle.load(open(file_path2, 'rb'))
# file_path3 = os.path.join(os.path.dirname(__file__), 'chatbot_Envo.h5')
file_path3 = 'static/chatbot_Envo.h5'
model = load_model(file_path3)
# file_path4 = os.path.join(os.path.dirname(__file__), 'intents.json')
file_path4 = 'static/intents.json'
intents = json.loads(open(file_path4).read())

def clean_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    result = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    result.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in result:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

class ChatResponse:
    @staticmethod
    def get_response(message):
        ints = predict_class(message)
        res = get_response(ints, intents)
        return res