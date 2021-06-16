import csv
import pandas as pd 
import numpy as np

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html


df=pd.DataFrame([[4,9]]*3,columns=['A','B'])
print(df)

a=df.apply(np.sqrt,axis=0)
print(a)

a=df.apply(lambda x: [1, 2], axis=1)
print(a)

#check Map.py for more info

np_array=[[ [2,4],[3,4] ]]*10
print(np_array)

df = pd.DataFrame(np_array, columns=['Column1', 'Column2'])

a=df.apply(lambda x: [*map(lambda y: y[1]-y[0], x)] )

print(a)
