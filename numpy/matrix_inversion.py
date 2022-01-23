import numpy as np

n=5

a=np.random.rand(n,n)
b=np.linalg.inv(a)

print(b)