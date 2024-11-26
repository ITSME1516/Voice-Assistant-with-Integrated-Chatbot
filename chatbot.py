import random
import json
import numpy as np
import pickle
import pyttsx3
import nltk
import re
import pyautogui as p
import AppOpener as a
import webbrowser as web
import time
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmetizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')

def clean_up_sentence(sentence):
    sentence_word = nltk.word_tokenize(sentence)
    sentence_word = [lemmetizer.lemmatize(word) for word in sentence_word]
    return sentence_word

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i , word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results =[[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x:x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intents': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intents']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result


engine = pyttsx3.init()
voice=engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('voice', voice[1].id)
def talk(out):
    engine.setProperty('volume', 100)
    engine.setProperty('rate', 150)
    engine.say(out)
    engine.runAndWait()

print("GO! BOT IS RUNNING!")

def get_res(message):
    
    if "open" in message:
        pat = r"\bopen\b"
        com = re.compile(pat)
        mat = com.search(message)
        point = mat.end()
        name = message[point:]
        a.open(name, match_closest = True)
        return "opening "+ name
    
    
    else:
        #message = input("")
        ints = predict_class(message)
        res = get_response(ints, intents)
        return str(res)
       

