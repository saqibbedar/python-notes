import pandas as pd

data_list = [1,2,3,4,5,None,6]
labels = ['a','b','c','d','e','f','g']

series = pd.Series(data_list, index=labels)

print(series)