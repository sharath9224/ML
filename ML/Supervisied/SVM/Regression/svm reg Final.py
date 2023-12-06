# necessary Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv('Admission_Prediction.csv')
#print(df.head())

print("NaN Values list before Cleaning \n",df.isna().sum())

# As we can see, there are some column with missing values. we need to impute those missing values.
df['GRE Score'].fillna(df['GRE Score'].mean(),inplace=True)
df['TOEFL Score'].fillna(df['TOEFL Score'].mean(),inplace=True)
df['University Rating'].fillna(df['University Rating'].mode()[0],inplace=True)

# seeing that after imputation no column has missing values
print("NaN Values list after Cleaning \n",df.isna().sum())
#print(df['University Rating'].head(10))

x=df.drop(['Chance of Admit','Serial No.'],axis=1) # df.iloc[:,1:-1]
y=df['Chance of Admit']

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2, random_state=0)

#importing the  model
from sklearn.svm import SVR
svr= SVR(C=1)
svr.fit(train_x, train_y)
pred_y=svr.predict(test_x)
# Accuracy test
from sklearn.metrics import r2_score
from sklearn import metrics
rmse = np.sqrt(metrics.mean_squared_error(test_y, pred_y))
print("RMSE Score :",rmse)

score= r2_score(test_y,svr.predict(test_x))
print("R2 Score : ",score)
