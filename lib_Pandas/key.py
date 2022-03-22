import csv
import pandas as pd 
import numpy as np
#playlist: https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
#https://youtu.be/W9XjRYFkkyw

filename='csv_demo'

#***start of reading the csv file using pandas*****************
print("reading the csv using lib pandas")
df=pd.read_csv(filename+'.csv')  	#data is a dataframe. 
        
print(df.keys())
print(df.keys()[0])
print(type(df.keys()[0]))