import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

#https://youtu.be/75mdKyA76i8
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html

A=2.
x0=1.
sigma=0.5

x=np.arange(0,2,0.0001)
y=A*np.exp(-((x-x0)/sigma)**2.)

peaks,properties=find_peaks(y,height=0.5)

print('peaks_index: '+str(peaks))
print('peaks: '+str(x[peaks]))
print('properties: '+str(properties))


plt.clf()
plt.plot(x,y)
plt.axvline(x[peaks],color='red',alpha=0.2,label='peak')
plt.axhline(properties['peak_heights'],color='green',alpha=0.2,label='height')

plt.show()


