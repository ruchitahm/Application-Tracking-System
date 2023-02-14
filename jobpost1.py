import nltk
import sklearn
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import OrderedDict
from nltk import ne_chunk,pos_tag
import sys, math, re
from operator import itemgetter
import math
import pickle
import string

file2 = open('op.txt','r')
data1 = file2.read()
print(data1)
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(data1)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
pos=nltk.pos_tag(filtered_sentence)
print(pos)

ne=nltk.ne_chunk(pos)
ne.draw()

from sklearn.feature_extraction.text import TfidfVectorizer
corpus =[data1]
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_
print (dict(zip(vectorizer.get_feature_names(), idf)))
with open('jobpost.pkl', 'wb') as f:
   pickle.dump(filtered_sentence, f)
