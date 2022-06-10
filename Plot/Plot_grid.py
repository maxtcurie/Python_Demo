import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,6,0.001)
y=np.sin(x)

plt.clf()
plt.plot(x,y)
plt.grid(alpha=0.5)
plt.show()
