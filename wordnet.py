from __future__ import division
import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from collections import OrderedDict
from nltk import ne_chunk,pos_tag

print("")
syns = wordnet.synsets("programmer")

#synset
print(syns[0].lemmas()[0].name())


#defintn
print(syns[0].definition())

print("")

synonyms=[]
antonyms=[]

for syn in wordnet.synsets("programmer"):
     for l in syn.lemmas():
         synonyms.append(l.name())
         #if l.antonyms():
          #   antonyms.append(l.antonyms()[0].name())
print(set(synonyms))
print("")
'''
print(set(antonyms))
print("")
'''
w1 = wordnet.synset("programmer.n.01")
w2 = wordnet.synset("coder.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("designer.n.01")
w2 = wordnet.synset("programmer.n.01")
print(w1.wup_similarity(w2))
'''
corpus = {
'a' : "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
'b' : "Professor Plum has a green plant in his study.",
'c' : "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."}

ordered_corpus = OrderedDict(sorted(corpus.items(), key = lambda t:t[0] ))
print (ordered_corpus)
text_list = [ y.lower().split() for x,y in ordered_corpus.items()]
nltk_repr = nltk.TextCollection(text_list)
term = 'green'
idx = 0
for title, text in ordered_corpus.items():
    score = 0
    score += nltk_repr.tf(term,text_list[idx] )
    idx += 1
    print ('tf score for ' + title + ' '+ 'is' +' ' + str(score))
idx = 0
for title, text in ordered_corpus.items():
    score = 0
    score += nltk_repr.tf_idf(term,text_list[idx] )
    idx += 1
    print ('tf_idf score for ' + title + ' '+ 'is' +' ' + str(score))
#print ('idf of "',term,'"  for corpus is ' ,nltk_repr.idf(term,text_list))

def tf_the_hard_way():
    pass

def idf_the_hard_way():
    pass

def tf_idf_the_hard_way():
    pass

print("")
print("")
print("")
'''
