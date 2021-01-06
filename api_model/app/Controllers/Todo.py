import json
from tensorflow import keras
from keras.preprocessing.sequence import pad_sequences
import numpy as np
from pickle import dump, load

# Khai báo từ điển
with open(r'app\Controllers\vocal_train.json',) as tf:
  vocal_train = dict(json.load(tf)) 
with open(r'app\Controllers\vocal_label.json',) as tf:
  vocal_label = dict(json.load(tf)) 
with open(r'app\Controllers\index_to_word.json',) as tf:
  index_to_word = dict(json.load(tf)) 

# Khai báo embedding 2 cái từ điển
embedding_matrix_train = load(open(r"app\Controllers\embedding_matrix_train.pkl", "rb"))
embedding_matrix_label = load(open(r"app\Controllers\embedding_matrix_label.pkl", "rb"))

# Khai báo model enconder và decoder
model1 = keras.models.load_model('app\Controllers\model_encoder')
model = keras.models.load_model('app\Controllers\model_decoder')

# Hàm xóa dấu câu
def remove_accents(input_str):
  s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
  s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'  
  s = ''
  for c in input_str:
    if c in s1:
      s += s0[s1.index(c)]
    else:
      s += c
  return s

# Thế chữ cuỗi
def the_chu_cuoi(a, txt):
  a = a.split(' ')
  a[len(a)-1] = txt
  return ' '.join(a)

# Hàm dự đoán
def greedySearch(seq_test):
    if seq_test == '':
      return ''
    in_text = ''
    cau = seq_test.split(' ')
    seq_train = [vocal_train[word] for word in seq_test.split(' ') if word in vocal_train]

    for i in range(len(cau)):
        in_text += ' ' + cau[i]
        sequence = [vocal_train[w] for w in in_text.split() if w in vocal_train]

        sequence = pad_sequences([sequence], maxlen=40)

        features_inp = model1.predict(pad_sequences([seq_train], maxlen=40))

        yhat = model.predict([features_inp,sequence], verbose=0)
        yhat = np.argmax(yhat)
        word = index_to_word[str(yhat)]
        # print(word)
        if cau[i] == remove_accents(word): 
          in_text = the_chu_cuoi(in_text, word)
        # print(in_text)
    return in_text

# print(greedySearch('em be mang ao mau do'))



