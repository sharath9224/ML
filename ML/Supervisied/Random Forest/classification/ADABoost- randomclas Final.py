# import libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
# read data set
dataset = pd.read_csv('bill_authentication.csv')
print(dataset.head())
'''
# define X and y
X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
#print("Before applying Standard Scalar :")
#print(X_train)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
#print("After applying Standard Scalar :")
#print(X_train)

from sklearn.ensemble import BaggingClassifier,RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier,GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

#rc = BaggingClassifier(DecisionTreeClassifier(),n_estimators = 5)
#rc = AdaBoostClassifier(n_estimators=22,learning_rate=1)
#rc = GradientBoostingClassifier(max_depth=2,n_estimators =24,learning_rate=1.0)
#rc = RandomForestClassifier(n_estimators=5)
#rc = XGBClassifier()
'''
'''
rc.fit(X_train, y_train)
y_pred = rc.predict(X_test)
print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test, y_pred)*100)
'''#
#Finding the number of n_estimators
'''
for n in range(1,50):
      #rc =AdaBoostClassifier(n_estimators=n,learning_rate=1)
      rc = GradientBoostingClassifier(max_depth=2,n_estimators =n,learning_rate=1)
      rc.fit(X_train, y_train)
      y_pred = rc.predict(X_test)
      print("Accuracy for %s estimators :%s" %(n,accuracy_score(y_test, y_pred)))
'''
'''
#Applying Multiple algorithms at a time
bc = BaggingClassifier(DecisionTreeClassifier(),n_estimators = 5, random_state=0)
abc = AdaBoostClassifier(n_estimators=22,learning_rate=1)
gbc = GradientBoostingClassifier(max_depth=2,n_estimators =24,learning_rate=1.0)
xgbc = XGBClassifier()
rfc = RandomForestClassifier(n_estimators=5, random_state=0)
d1={}
for rc in bc,abc,gbc,xgbc,rfc:
      rc.fit(X_train, y_train)
      y_pred = rc.predict(X_test)
      d1[rc]=accuracy_score(y_test, y_pred)*100
      
for k,v in d1.items():
      print(k," : ",v)

'''
