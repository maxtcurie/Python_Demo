import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,6,0.01)
f=np.sin(x)
new_x=np.arange(0,6,0.001)
new_f=np.interp(new_x,x,f)
plt.clf()
plt.plot(x,f,label='original')
plt.plot(new_x,new_f,label='interp, 10time')
new_x=np.arange(0,6,0.5)
new_f=np.interp(new_x,x,f)
plt.plot(new_x,new_f,label='interp, 0.02time')
plt.legend()
plt.show()
