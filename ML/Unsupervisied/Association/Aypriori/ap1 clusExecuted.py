import numpy as np
import pandas as pd
from apyori import apriori

#/keeping header as None
store_data = pd.read_csv('store_data.csv', header=None)  
#print(store_data.head())
print(store_data.shape)

records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])
#print(records)

association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=4, min_length=5)
association_results = list(association_rules)

print(len(association_results)) # //to check the Total Number of Rules mined
#print(association_results[0])  #// to print the first item the association_rules list to see the first rule

#Total association rules
'''
for rule in association_results:
    print(rule)
'''
'''
# // to display the rule, the support, the confidence,
#     and lift for each rule in a more clear way:
for item in association_results:                                         

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])
'''

