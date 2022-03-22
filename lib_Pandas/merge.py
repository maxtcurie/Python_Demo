import csv
import pandas as pd 
import numpy as np
#useful website: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})


#df3=df1.join(df2)
#print(df3)

df3=pd.concat([df1, df2], axis=0)
print(df3)

df3 = df1.merge(df2, left_on='lkey', right_on='rkey',\
                suffixes=('_1', '_2'))
print(df3)


df3 = df1.merge(df2, how='inner',on='value') #how is similar to SQL
print(df3)



