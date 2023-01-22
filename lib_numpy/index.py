import numpy as np

#from: https://www.w3schools.com/python/numpy/numpy_array_filter.asp
arr=np.arange(10,dtype='int')

filter_arr = (arr % 2 == 0)

new_arr=arr[filter_arr]

print(arr)
print(new_arr)