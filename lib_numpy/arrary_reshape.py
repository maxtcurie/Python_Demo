import numpy as np

#https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape

x1=np.arange(0,4,1)
x2=np.arange(0,8,2)
x=np.array([x1,x2])

print(x)
print(np.shape(x))


np.reshape(x,(2,2,2),order='C')