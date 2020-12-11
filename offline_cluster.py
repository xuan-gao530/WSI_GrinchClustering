import sklearn
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from pathlib import Path

with open('glove.6B/glove.6B.100d.txt', encoding='utf-8') as ef:
	embeddings_dict = {}
	for line in ef:
		embeddings_dict[line.split()[0]] = np.array([float(value) for value in line.split()[1:]])

target_word = 'bank'
context_words = []
with open("toy_data.txt") as tf:
	for line in tf:
		words = [word.lower().strip('.,?') for word in line.split()]
		for i, word in enumerate(words):
			if word == target_word:
				context_words.extend(words[max(i-5, 0):i])
				context_words.extend(words[i+1:min(i+5, len(words))])
	

print(context_words)
context_embs = [embeddings_dict[cw] for cw in context_words]
context_embs = np.array(context_embs)
print(context_embs.shape)

clustering = AgglomerativeClustering(n_clusters=2, affinity='cosine', linkage='average').fit(context_embs)
labels = clustering.labels_

assert len(context_words) == len(labels)

cluster1 = [context_words[index] for index in range(len(labels)) if labels[index] == 0]
cluster2 = [context_words[index] for index in range(len(labels)) if labels[index] == 1]

print('0', cluster1)
print('1', cluster2)