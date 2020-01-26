# Libraries
import pickle
import numpy as np
from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding, Activation, Dropout, LSTM
from keras.models import Sequential
import re
import nltk
import inflect
from flask import Flask
from flask_cors import CORS, cross_origin
from keras.models import load_model

# Load\prepare model
texts = pickle.load(open("texts.p", "rb"))
model = load_model('model.h5')

# Initialize Flask
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/<path:text>')
@cross_origin()
def predict(text):
	from keras.models import load_model
	text = text.lower()
	text = re.sub("([a-z])('|’|\s)((t|n|ll|m|s|re|d)(\W|$))", "\g<1>\g<3>", text)
	text = re.sub("[^a-z0-9\s]", "", text)
	text = re.sub("[\s+]", " ", text)
	tokenizer = nltk.tokenize.RegexpTokenizer('(?<!\w)[A-Za-z0-9]+(?!\w)')  
	text = tokenizer.tokenize(text)     
	p = inflect.engine()
	for i, word in enumerate(text):
		if re.fullmatch("\d+", word) != None:
			word = p.number_to_words(word)
			word = word.replace("-", " ")
			text[i] = word
	text = " ".join(text)
	text = tokenizer.tokenize(text)
	tokenizer = Tokenizer(lower = False)
	tokenizer.fit_on_texts(texts)
	sequences = tokenizer.texts_to_sequences([text])
	x = pad_sequences(sequences, maxlen=15)
	y = model.predict(x)
	text = str(round(y[0][0]*100,0))[:-2]
	return text	
