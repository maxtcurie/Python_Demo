def sql_table_to_df(file_name):
	import pandas as pd
	import numpy as np
	f=open(file_name,"r")
	lines=f.readlines()
	
	name=(lines[1].replace(' ','')).split('|')[1:-1]
	
	data_lines=lines[3:-1]
	
	data_array=[]
	
	for line in data_lines:
		data_array.append((line.replace(' ','')).split("|")[1:-1])
	data_array=np.array(data_array)

	df=pd.DataFrame(data_array, columns = name) 

	return df
