#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sklearn
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from pathlib import Path
import string
import csv
with open('glove.6B.300d.txt', encoding='utf-8') as ef:
	embeddings_dict = {}
	for line in ef:
		embeddings_dict[line.split()[0]] = np.array([float(value) for value in line.split()[1:]])

        
def dataprocess():
        context_words_all = []
        dataset= ("twsi_test.csv")
        target_word='stage' 
        csv_file=open(dataset)    
        csvf = csv.reader(csv_file)
        for line in csvf:
            if (line[0]==target_word ):
                if line[1] == '2':
                    context_words = []
                    sentence=line[2].strip('[](),.')
                    punctuation_string = string.punctuation           # delete all punctuation
                    for j in punctuation_string:
                        sentence = sentence.replace(j, '')
                    words = [word.lower() for word in sentence.split()]
                    for i, word in enumerate(words):
                        if word == target_word:
                            context_words.extend(words[max(i-5, 0):i])
                            context_words.extend(words[i+1:min(i+5, len(words))])
                    context_words_all.append(context_words)
        return context_words_all

dataprocess()


def word_embedding(context_words):
        glovefile='glove.6B.300d.txt'
        with open(glovefile, encoding='utf-8') as ef:
            embeddings_dict = {}
            for line in ef:
                embeddings_dict[line.split()[0]] = np.array([float(value) for value in line.split()[1:]])

        data_stream=[]     #store the datapoint object  VectorDataPoint.id vector
        for cw in context_words:
            embedding_vector=embeddings_dict.get(cw)
            if embedding_vector is not None:
                data_stream.append(embedding_vector)
        return data_stream


# In[ ]:


l = word_embedding(dataprocess()[14])
    bank_gold = l
    from scipy import spatial

    lines = open("offline.txt", "rb").readlines()
    lines = [line.decode(errors='ignore').strip() for line in lines]
    for line in lines:
        a= np.loadtxt('offline.txt')
        list1 = []
        bank_online1 = a[8]
        bank_gold1 = np.array(bank_gold)
        bank_gold2 = np.mean(bank_gold1,axis = 0)
        result = 1 - spatial.distance.cosine(bank_online1, bank_gold2)
        print(result)

