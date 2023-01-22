import numpy as np
import matplotlib.pyplot as plt

#from: https://www.geeksforgeeks.org/calculate-the-euclidean-distance-using-numpy/

x=np.arange(-2,2,0.001)
y1=np.sin(x)
y2=np.zeros(len(x))

X1=np.array([x,y1]).T
X2=np.array([x,y2]).T

dis=np.linalg.norm(X1 - X2, axis=1)
print(dis)