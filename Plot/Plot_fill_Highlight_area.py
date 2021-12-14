import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x_min=0
x_max=1
y_min=2
y_max=3
x_fill=[x_min,x_min,x_max,x_max]
y_fill=[y_min,y_max,y_max,y_min]


plt.clf()
plt.fill(x_fill,y_fill,alpha=0.6,label='highlight')
plt.legend()
plt.show()

