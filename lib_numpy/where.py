import numpy as np

#https://numpy.org/doc/stable/reference/generated/numpy.where.html
x=np.arange(0,10,1)
y=np.arange(0,100,10)

x_out=np.where(x>=3,x,y)
print(x_out)


