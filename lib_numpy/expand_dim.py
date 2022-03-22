import numpy as np

a=np.random.rand(3,3,3)
a1=np.expand_dims(a,axis=3)
print(np.shape(a1))
