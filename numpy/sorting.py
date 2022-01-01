import numpy as np

a = np.array([[1,4], [3,1]])
print(a)
#sorting all the 
b=np.sort(a,axis=-1)
print(b)
a.sort(axis=-1)
print(a)