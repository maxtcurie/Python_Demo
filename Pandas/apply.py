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
