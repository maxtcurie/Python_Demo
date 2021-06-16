import csv
import pandas as pd 
import numpy as np

#from: https://www.marsja.se/how-to-convert-numpy-array-to-pandas-dataframe-examples/


np_array=[[2,4]]*10
print(np_array)

df = pd.DataFrame(np_array, columns=['Column1', 'Column2'])


