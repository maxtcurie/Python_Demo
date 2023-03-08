import csv
import pandas as pd 
import numpy as np
#playlist: https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
#https://youtu.be/W9XjRYFkkyw

#useful website: https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html

filename='csv_demo'

#***start of reading the csv file using pandas*****************
print("reading the csv using lib pandas")
data=pd.read_csv(filename+'.csv')  	#data is a dataframe. 
        #pd.read_csv(csvfile_name).drop(['unnamed 0'],axis=1) for dropping the index
print(data)

#https://towardsdatascience.com/8-ways-to-filter-pandas-dataframes-d34ba585c1b8
df=data.query('x>0 and x<0.1 ')

print(df)

df=data[((data.x < -1) | (data.x > 2))]
print(df)


#https://swdevnotes.com/python/2021/how-to-filter-a-pandas-dataframe/
data=data.astype({'x':'str'})

print(data)

df=data[data.x.str.contains('52', case=False, na=False)]
print(df)