import numpy as np
import matplotlib.pyplot as plt


x=np.arange(-2,2,0.001)
y=np.sin(x)

plt.clf()
plt.plot(x,y,label='y')
plt.plot(x,np.gradient(y,x),label='dy')
plt.plot(x,np.gradient(np.gradient(y,x),x),label='ddy')
plt.legend()
plt.show()