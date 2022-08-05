import numpy as np 

a=np.random.rand(2,4)
print(a)

a_sum=a.sum(axis=0) #sum over the columns
print(a_sum)

a_percent=100*a/a_sum
print(a_percent)

#the a_sum becomes the 2X4 matrix in operation, such a automatic transformation is called boardcasting