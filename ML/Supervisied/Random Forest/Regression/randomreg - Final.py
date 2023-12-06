import pandas as pd
import numpy as np
from sklearn import metrics

dataset = pd.read_csv('petrol_consumption.csv')
X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 4].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from xgboost import XGBRegressor

#rr = RandomForestRegressor(n_estimators=5,random_state=0)
#rr = GradientBoostingRegressor(max_depth=2,n_estimators =8,learning_rate=1.0)
#rr= AdaBoostRegressor(n_estimators = 32,learning_rate=1)
#rr = XGBRegressor()
'''
rr.fit(X_train, y_train)
y_pred = rr.predict(X_test)
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
'''
#Finding the number of n_estimators
'''
for n in range(1,50):
      rr =AdaBoostRegressor(n_estimators=n,learning_rate=1)
      rr.fit(X_train, y_train)
      y_pred = rr.predict(X_test)
      print("RMSE for %s estimators :%s" %(n,np.sqrt(metrics.mean_squared_error(y_test, y_pred))))
'''
'''
for n in range(1,25):
      rr =GradientBoostingRegressor(max_depth=1,n_estimators =n,learning_rate=1)
      rr.fit(X_train, y_train)
      y_pred = rr.predict(X_test)
      print("RMSE for %s estimators :%s" %(n,np.sqrt(metrics.mean_squared_error(y_test, y_pred))))
'''
'''
rfr = RandomForestRegressor(n_estimators=5,random_state=0)
gbr = GradientBoostingRegressor(max_depth=1,n_estimators =8,learning_rate=1.0)
xgb_r = XGBRegressor()
abr= AdaBoostRegressor(n_estimators = 5,learning_rate=1,random_state=0)
d1={}

for rr in rfr,gbr,xgb_r,abr:
    rr.fit(X_train, y_train)
    y_pred = rr.predict(X_test)
    d1[rr]= np.sqrt(metrics.mean_squared_error(y_test, y_pred))

for k,v in d1.items():
    print(k," : ",v)
'''



    
