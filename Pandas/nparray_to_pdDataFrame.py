import csv
import pandas as pd 
import numpy as np

#from: https://www.marsja.se/how-to-convert-numpy-array-to-pandas-dataframe-examples/


np_array=[[2,4]]*10
print(np_array)

df = pd.DataFrame(np_array, columns=['Column1', 'Column2'])

print(df)

print('**************')

x=np.arange(0,1,0.001)
y=np.sin(x)
df=pd.DataFrame(list(zip(x, y)), columns=['x', 'sin(x)'])

print(df)
