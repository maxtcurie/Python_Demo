import numpy as np

X=np.random.rand(200,8,8,3)


X_flatten = X.reshape(X.shape[0], -1).T 

print(np.prod(np.shape(X)[1:]))

print(np.shape(X_flatten))