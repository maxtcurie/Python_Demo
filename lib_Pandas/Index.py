import csv
import pandas as pd 
import numpy as np
#playlist: https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
#https://youtu.be/W9XjRYFkkyw

filename='csv_demo'

#***start of reading the csv file using pandas*****************
print("reading the csv using lib pandas")
df=pd.read_csv(filename+'.csv')  	#data is a dataframe. 
        #pd.read_csv(csvfile_name).drop(['unnamed 0'],axis=1) for dropping the index


print(df)

print('df.set_index(y)')
df.set_index('y')
print(df)

print('df.set_index(y,inplace=True)')
df.set_index('y',inplace=True)
print(df)

print('df.sort_index(y)')
print(df.sort_index())

print('print df')
print(df)

print('df.sort_index(y,inplace=True)')
df.sort_index(inplace=True)
print(df)

print('df.reset_index(inplace=True)')
df.reset_index(inplace=True)
print(df)

#multi indexes
#https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex
arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))
MultiIndex([(1,  'red'),
            (1, 'blue'),
            (2,  'red'),
            (2, 'blue')],
           names=['number', 'color'])
pd.MultiIndex.from_arrays(arrays, names=('number', 'color'))