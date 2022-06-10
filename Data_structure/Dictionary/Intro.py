#data structure:https://docs.python.org/3/tutorial/datastructures.html


#dict

#Dictionary
{x: x**2 for x in (2, 4, 6)}

thisdict = {
  "a": 2,
  "b": 3,
  "c": 1
}

print('thisdict')
print(thisdict)
print('list(thisdict)')
print(list(thisdict))
print('thisdict.items()')
print(thisdict.items())

print(thisdict.keys())
print(thisdict.values())

for key,value in thisdict.items():
  print(key,value)


#dict to dataframe
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html
#https://www.geeksforgeeks.org/how-to-convert-dictionary-to-pandas-dataframe/
import pandas as pd

#example 1
df = pd.DataFrame.from_dict(thisdict, orient ='index') 
print(df)


#example 2
data = [{'area': 'new-hills', 'rainfall': 100, 'temperature': 20},
         {'area': 'cape-town',  'rainfall': 70, 'temperature': 25},
         {'area': 'mumbai',  'rainfall': 200,  'temperature': 39 }]
df = pd.DataFrame.from_dict(data)
print(df)




