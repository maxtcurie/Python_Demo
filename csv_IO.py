import csv
import pandas as pd 
import numpy as np


filename='csv_demo'

x=np.arange(0.,7.,0.001)	#x grid from 0 to 7 with resolution of 0.001
y=np.sin(x)					#y=sin(x)


#from https://docs.python.org/3/library/csv.html

#****start of writting the csv file using csv********************
print("writting the csv using lib csv")
with open(filename+'.csv', 'w') as csvfile:		#clear all and then write a row
    data = csv.writer(csvfile, delimiter=',')
    data.writerow(['x','y'])
csvfile.close()

with open(filename+'.csv', 'a') as csvfile:	#adding a row
    data = csv.writer(csvfile, delimiter=',')
    for i in range(len(x)):	#loop through x
        data.writerow([x[i],y[i]])
csvfile.close()
#****end of writting the csv file using csv********************

#****start of reading the csv file using csv********************
print("reading the csv using lib csv")
with open(filename+'.csv', newline='') as csvfile:		#clear all and then write a row
    data = csv.reader(csvfile, delimiter=',')	
    print(data)	#data is a object
    i = 0
    for row in data:
    	i=i+1
    	if i%2==1:
    		a=0
            #print(row)      
csvfile.close()
#****end of reading the csv file using csv*********************


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