import csv
import pandas as pd 
import numpy as np
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html

filename='csv_demo'

#***start of reading the csv file using pandas*****************
print("reading the csv using lib pandas")
df=pd.read_csv(filename+'.csv')  	#data is a dataframe. 
        #pd.read_csv(csvfile_name).drop(['unnamed 0'],axis=1) for dropping the index


print(df)

print('*****************')
print(df.loc[1])#info of 1st row
print('*****************')
print(df.loc[ [1,0] ])#info of 1st row and 0th row
print('*****************')
print(df.loc[ 1,'x' ])#info of 1st, row 'x' column
#print('df.info()='+str(df.info()))
#print('df.info()[0]='+str(df.info()[0]))

