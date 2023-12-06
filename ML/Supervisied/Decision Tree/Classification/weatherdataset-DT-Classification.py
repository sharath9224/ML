import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics, tree
from sklearn.tree import DecisionTreeClassifier

dt = pd.read_csv('weather.csv')
print(dt)

dt['play'],_= pd.factorize(dt['play'])
dt['outlook'],_= pd.factorize(dt['outlook'])
dt['temperature'],_= pd.factorize(dt['temperature'])
dt['humidity'],_=pd.factorize(dt['humidity'])
dt['windy']=pd.factorize(dt['windy'])[0]
#dt['windy'],_=pd.factorize(dt['windy'])

X = dt.iloc[:,:-1] 
y = dt.iloc[:,-1] # Only last col
print(X)

# split data randomly into 80% training and 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# train the decision tree
#dtree = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=3)
#dtree = DecisionTreeClassifier(criterion = 'entropy')
#dtree = tree.DecisionTreeClassifier(criterion = 'gini', max_depth=3)
dtree = DecisionTreeClassifier(criterion = 'gini')

dtree.fit(X_train, y_train)

# use the model to make predictions with the test data
y_pred = dtree.predict(X_test)
#print(y_pred)

# Making the Confusion Matrix
cm = metrics.confusion_matrix(y_test, y_pred)
print("Confusion MAtrix:",cm)
print('Accuracy :',metrics.accuracy_score(y_test, y_pred))


