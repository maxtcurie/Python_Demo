import numpy as np
import matplotlib.pyplot as plt

#https://matplotlib.org/3.1.1/gallery/ticks_and_spines/multiple_yaxis_with_spines.html

x=np.arange(0,6,0.001)
y1=np.sin(x)**2.
y1_error=y1*0.1
y2=2.*np.cos(x)**2.
y2_error=y2*0.1
y3=20.*np.cos(2.*x)**2.

labels=['y1','y2']
fig, ax1=plt.subplots(nrows=1,ncols=1,sharex=True) 
line1=ax1.errorbar(x,y1,yerr=y1_error, color='b', label='y1')

# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_xlabel('x')
ax1.set_ylabel('y1', color='b')
ax1.tick_params('x', colors='b')

ax2 = ax1.twinx()
line2=ax2.errorbar(x,y2,yerr=y2_error, color='r', label='y2')
ax2.set_ylabel('y2', color='r')
ax2.tick_params('x', colors='r')

ax1.legend([line1, line2], labels)

fig.tight_layout()
plt.show()