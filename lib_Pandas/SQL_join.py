import csv
import pandas as pd 
import numpy as np

filename='csv_demo'

#***start of reading the csv file using pandas*****************
print("reading the csv using lib pandas")
df=pd.read_csv(filename+'.csv')  	#data is a dataframe. 
        #pd.read_csv(csvfile_name).drop(['unnamed 0'],axis=1) for dropping the index

#similar to JOIN in SQL

merg1=pd.merge(left = df, right = df, how = 'left', on='x',\
        suffixes=('_l','_r'))
print(merg1)