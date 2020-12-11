# WSI_GrinchClustering
----CSCI 5454 Algorithm Project
## Team member: Ananya Ganesh, Xuan Gao, Changbing Yang
## Environment: Python 3.7
## Introduction
 In this project, we adopt an online algorithm, which presents an incremental algorithm for hierarchical clustering called GRINCH[1] to perform on WSI. We understand this algorithm by evaluating its performance on TWSI benchmark and further make a comparison with offline algorithms.For the implementation of Grinch, we use the code from github[2].We implement the code of processing the input, output and evaluation. The details are listed in the next.
## Structure of this project 
1. packages from the github code[2]
*clustering: the clustering algorithm (i.e. Grinch, Rotation, Online) and the function to calculate dendrogram purity.
*dendrogram: the definition of dendrogram tree.
*model: the definition of clusters and data points used in clustering.
*linkage: some predefined linkage function
*monitor: contains the dendrogram purity monitor which is used to track the dendrogram purity change during HAC clustering.
*nsw: the definition of nearest neighbor small world graph which is used to implement the navigable small world graph approximation of Grinch algorithm.
(We didn't use the package gendataset:we've defined our own dataset.)
*requirements.txt: package list needed to be installed

2.Our implementation
* twsi_train.csv, twsi_test.csv: dataset created from twsi[3]
* glove.6B.300d.txt[4] :Word embedding file
* grinchcluster.ipynb : codes for online clustering, including processing dataset input, output for evaluation, falting the clusters and clustering visualization.
* offline_cluster.py: code for offline clustering using HAC
* Evaluation.py: code for evaluation
* output folder: output txt files for online and offline algorithm. It also includes some graphs for grinch algorithm.

 
## Citation:
[1]Nicholas Monath et al. “Scalable Hierarchical Clustering with Tree Grafting”. In:Proceedings of the 25th ACMSIGKDD International Conference on Knowledge Discovery & Data Mining. 2019, pp. 1438–1448.
[2]Implementation of Grinch, https://github.com/Troublor/grinch
[3]C. Biemann and V. Nygaard (2010): Crowdsourcing WordNet. In Proceedings of the 5th Global WordNet conference, Mumbai, India. , ACL Data and Code Repository, ADCR2010T006, http://aclweb.org/aclwiki.
[4]Jeffrey Pennington, Richard Socher, and Christopher D. Manning. 2014. GloVe: Global Vectors for Word Representation.
