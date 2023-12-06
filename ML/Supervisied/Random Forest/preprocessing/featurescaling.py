#Example for MinMaxScaler and StandadScaler
import pandas as pd
import numpy as np

df = pd.read_csv("iris.csv")
print(df.head())

# Using Normalization- MinMaxScaler
# Normalization scale down the values 0-1
'''
from sklearn.preprocessing import MinMaxScaler
scaling=MinMaxScaler()

print(scaling.fit_transform(df[["sepal_length","sepal_width"]]))

'''
# Using Standization - StandardScaler
# StandardScaler scale values as mean is zero and standard deviation is 1

from sklearn.preprocessing import StandardScaler
scaling=StandardScaler()
#df["sepal_length"]=scaling.fit_transform(df["sepal_length"])
#df["sepal_width"]=scaling.fit_transform(df["sepal_width"]))

print(scaling.fit_transform(df[["sepal_length","sepal_width"]]))

