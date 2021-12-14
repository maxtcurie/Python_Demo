import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd



c = 4.2
m = 200
alpha = 1
PHeat = 600
T0 = 21

x=np.arange(0,200,1)
y=(T0 + (alpha *PHeat* x)/(c *m))
#C to F conversion
y=y*9./5.+32.

plt.clf()
plt.plot(x,y,label='Theory')
plt.plot(x,y,label='Experiment')
plt.show()