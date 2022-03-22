#dict to dataframe
import pandas as pd

np_array=[[2,4]]*10
print(np_array)

df = pd.DataFrame(np_array, columns=['Column1', 'Column2'])
print(df)