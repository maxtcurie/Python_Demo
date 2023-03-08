import numpy as np

X=np.random.rand(200,8,8,3)


X_flatten = X.reshape(X.shape[0], -1).T 

print(np.prod(np.shape(X)[1:]))

print(np.shape(X_flatten))

##from: https://stackoverflow.com/questions/1550130/cloning-row-or-column-vectors
a=np.tile(np.array([1,2,3]), (3, 1))
print(a)

a=np.array([[2,4,6],]*3)
print(a)
