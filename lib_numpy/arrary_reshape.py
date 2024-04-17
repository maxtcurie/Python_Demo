import numpy as np

#https://numpy.org/doc/stable/reference/generated/numpy.reshape.html#numpy.reshape

x1=np.arange(0,4,1)
x2=np.arange(0,8,2)
x=np.array([x1,x2])

print(x)
print(np.shape(x))


x=np.reshape(x,(2,2,2),order='C')

print(x)
print(np.shape(x))

original_array=np.random.rand(3,4,5,6)

flatten_array = original_array.reshape(-1, *original_array.shape[2:])
print(flatten_array)
print(np.shape(flatten_array))