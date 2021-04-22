import csv
import pandas as pd 
import numpy as np


filename='csv_demo'

x=np.arange(0.,7.,0.001)	#x grid from 0 to 7 with resolution of 0.001
y=np.sin(x)					#y=sin(x)


#***start of writting the csv file using pandas*****************
print("writting the csv using lib pandas")
d = {'x':x,'y':y}
df=pd.DataFrame(d, columns=['x','y'])	#construct the panda dataframe
df.to_csv(filename+'.csv',index=False)
#***end of writting the csv file using pandas*****************

#***start of reading the csv file using pandas*****************
print("reading the csv using lib pandas")
data=pd.read_csv(filename+'.csv')  	#data is a dataframe. 
        #pd.read_csv(csvfile_name).drop(['unnamed 0'],axis=1) for dropping the index
x=data['x']
y=data['y']
print(data)
#print(x)
#print(y)
#***end of reading the csv file using pandas*****************