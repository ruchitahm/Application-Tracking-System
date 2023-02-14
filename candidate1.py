from __future__ import division
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
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
'''
Pos tags

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
'''

import string
file1 = open('op3.txt','r')
data = file1.read()
print(data)
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(data)

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
corpus =[data]
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_
print (dict(zip(vectorizer.get_feature_names(), idf)))
#

##job_reqs = ["java", "python"]
with open('jobpost.pkl', 'rb') as f:
   job_reqs = pickle.load(f)

#job_reqs_c = len(job_reqs)+1
count = 0
new_filtered_list = list(set(filtered_sentence))

for i in range(len(new_filtered_list)):
    if new_filtered_list[i] in job_reqs:
        #print new_filtered_list[i]
        count += 1

suit_per = count / len(job_reqs)
print ((count, job_reqs))

print ("Candidate is suitable: "+str(suit_per*100)+"%")


# x-coordinates of left sides of bars
##left = [1, 2, 3, 4, 5]
left = range(1,len(job_reqs)+1)

# heights of bars
##height = [10, 24, 36, 40, 5]
height = []
for i in range(len(job_reqs)):
    if i >= count:
        height.append(0)
    else:
        height.append(1)
print (height)

# labels for bars
##tick_label = ['one', 'two', 'three', 'four', 'five']
tick_label = job_reqs


# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('Similarity chart')

# function to show the plot
plt.show()
