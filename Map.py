#From: https://www.geeksforgeeks.org/python-map-function/

# Python program to demonstrate working
# of map.
  
# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

import numpy as np
a=np.arange(10)
b=np.zeros((10,5,2))
for i in range(10):
	for j in range(5):
		b[i,j,:]=[2,4]
print(b)
#a=np.arange(len(numbers))
result = map[lambda x: [*map(lambda y: y[1]-y[0], x)] , b]
print(*result)