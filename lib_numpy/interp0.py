import numpy as np

x=np.arange(0,6.00001,0.001)
y=np.sin(x)

x2=np.arange(0,6.00001,0.0002)
y2=np.interp(x2,x,y)

import matplotlib.pyplot as plt

plt.clf()
plt.plot(x,y,  label='original')
plt.plot(x2,y2,label='interp')
plt.legend()
plt.show()