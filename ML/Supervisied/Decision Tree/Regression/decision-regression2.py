# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics,tree

df = pd.read_csv('train.csv')
print(df.head())

x = df.iloc[:,1:2]
y = df.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=40)

# Finding the Accuracy by means of Max_depth
'''
for i in range(1,20):
      dtree = DecisionTreeRegressor(max_depth=i)
      dtree.fit(x_train,y_train)
      y_pred = dtree.predict(x_test)
      rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
      print("RMSE Score---",i,":",rmse)
'''
dtree = DecisionTreeRegressor(max_depth=2)
#dtree = tree.DecisionTreeRegressor(max_depth=2)
dtree.fit(x_train,y_train)
y_pred = dtree.predict(x_test)
#print(y_pred)

rmse = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
print("RMSE Score :",rmse)


