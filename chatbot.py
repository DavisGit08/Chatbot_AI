# Using natural language proccessing and neuronal networks in python
import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer # nltk is a platform for building Python programs to work with human language data
from tensorflow.python.keras.models import load_model # TensorFlow is a learning model

lemmatizer = WordNetLemmatizer() #new instance of the WordNetLemmatizer class
intents = json.loads(open('intents_spanish.json', 'r', encoding='utf-8').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def clean_up_sentence(sentence): # Clean up the user's input
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == 0:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_TRESHOLD = 0.25 # umbral del error, 25%
    results = [[i,r] for i, r in enumerate(res) if r > ERROR_TRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0] ['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result
