import numpy as np


a=[1, 3, 4, 3]
b=[3, 1, 2, 1]
overlap_arr=np.intersect1d(a,b)
print(overlap_arr)

a=[1, 3, 4, 3]
b=[3, 1, 2, 1, 3]
overlap_arr=np.intersect1d(a,b)
print(overlap_arr)

