#dict to dataframe
import pandas as pd

name_list=['Column1']
dtype_list=['string']

np_array=[[2,4]]*10
print('*****************')
print(np_array)

df = pd.DataFrame(np_array, columns=['Column1', 'Column2'])
print('*****************')
print(df)

convert_dict = {}
for (name,type_) in zip(name_list,dtype_list):
	convert_dict[name]=type_
df=df.astype(convert_dict)
print('*****************')
print(df.Column1)
print('*****************')
print(df.dtypes)
print('*****************')
print(df)