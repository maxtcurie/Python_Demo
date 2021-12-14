import csv
import pandas as pd 
import numpy as np
#playlist: https://www.youtube.com/watch?v=ZyhVh-qRZPA&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS
#https://youtu.be/ZyhVh-qRZPA

filename='csv_demo'

#***start of reading the csv file using pandas*****************
print("reading the csv using lib pandas")
df=pd.read_csv(filename+'.csv')  	#data is a dataframe. 
        #pd.read_csv(csvfile_name).drop(['unnamed 0'],axis=1) for dropping the index

print(df)
print('df.shape='+str(df.shape))
df.info()
pd.set_option('display.max_columns',1) #print out 1 columns of the data

print(df)
#print('df.info()='+str(df.info()))
#print('df.info()[0]='+str(df.info()[0]))

