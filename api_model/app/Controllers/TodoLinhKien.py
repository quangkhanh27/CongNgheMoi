from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Embedding
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import LSTM
from keras.initializers import Constant
from keras.layers.wrappers import Bidirectional
from pickle import dump, load
import json
from keras.preprocessing.sequence import pad_sequences

import numpy as np

from underthesea import word_tokenize

embedding_matrix = load(open(r"app\Controllers\embedding_matrix.pkl", "rb"))

model = Sequential()
model.add(Embedding(4616, 300, embeddings_initializer=Constant(embedding_matrix),
    input_length=80))
model.add(Bidirectional(LSTM(64, dropout = 0.2, recurrent_dropout = 0.2)))
model.add(Flatten())
model.add(Dense(5000, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.load_weights('app\Controllers\model_linhKien.h5')


file = open(r'app\Controllers\list_CORPUS.txt', encoding="utf8")
list_CORPUS = file.read().split('\n')
file.close()

def predict(s):
    if s == '':
        return ''
    s = word_tokenize(s, format='text').split()
    vec = []
    for i in s:
        if i not in list_CORPUS:
            vec.append(0)
        else:
            vec.append(list_CORPUS.index(i))
    list_test = []
    list_test.append(vec)
    s = pad_sequences(list_test, maxlen = 80, truncating = 'post', padding = 'post')
    return str(np.argmax(model.predict(s)))
