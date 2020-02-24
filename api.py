from flask import Flask, request, render_template, jsonify
import json
import requests
import pandas as pd
from pandas.io.json import json_normalize

## Toxicity Model Files
import numpy as np

#from keras.models import Sequential
from keras.models import model_from_json

from keras.preprocessing import sequence
import keras.preprocessing.text as txt
from keras.preprocessing.text import Tokenizer
import pickle
import os
import tensorflow as tf

# loading Tokenizer
tok = Tokenizer(oov_token = True)
with open(os.path.expanduser('~/Python_Work/Deployment_001/Projects/api_007/Models/tokenizer_200d_1M_10.pickle'), 'rb') as handle:
    tok = pickle.load(handle)

#Loading Model
with open(os.path.expanduser('~/Python_Work/Deployment_001/Projects/api_007/Models/best_model_200d_1M_10_in_json.json'),'r') as f:
    model_json_new = json.load(f)

loaded_model = model_from_json(model_json_new)
loaded_model.load_weights(os.path.expanduser('~/Python_Work/Deployment_001/Projects/api_007/Models/best_model_200d_1M_10.h5'))
graph = tf.get_default_graph()

max_tweet_length = 50
def text_to_sequence(list_indices):
    # Looking up words in dictionary
    words = [tok.word_index.get(wrd) for wrd in list_indices]
    return(words)

def test_tweet(tweet):
    # Convert tweet into sequence of words and pass it through filters.
    # fitlers are used to remove special characters which are increasing complexity in the structure of the sentence.
    test = txt.text_to_word_sequence(tweet, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=' ')
    # To process with text, we need to convert this sequence of words to numbers
    test = text_to_sequence(test)
    # If words are not found in word dictionary, assigned number to the words will be None. We need to remove all these None.
    test = [0 if v is None else v for v in test]
    # Make sequence to the pre-defined sequence length.
    test = sequence.pad_sequences([test], maxlen=max_tweet_length)
    # Convert numbers to the specific datatype format, if not.
    test = np.asarray(test)
    # Predict the toxicity from our model.
    pred = loaded_model.predict(test)
    # Return the result
    return json.dumps(str(pred[0][0]))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/process', methods=['GET', 'POST'])
def my_data():
    global graph
    text = request.form['inpt']
    word = request.args.get('inpt')

    with graph.as_default():
        result_output = test_tweet(text)

    result = {
        "TOXICITY": result_output
    }
    data3 = {
        "input": text
    }

    return jsonify(result = result, data=data3)

if __name__ == '__main__':
    app.run(debug=True)