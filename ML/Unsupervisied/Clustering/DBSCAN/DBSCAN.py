# DBSCAN Clustering
# Importing the libraries
import numpy as np
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]]
print(X)

from sklearn.cluster import DBSCAN
dbscan=DBSCAN(eps=5,min_samples=6)

# Fitting the model
model=dbscan.fit(X)

labels=model.labels_
print("the label are :",labels)

#from sklearn import metrics

print('Length :',len(set(labels)))

#Calculating the number of clusters
n_clusters=len(set(labels))- (1 if -1 in labels else 0)
print("Number of clusters : ",n_clusters)



