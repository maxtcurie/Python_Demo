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



#from: https://stackoverflow.com/questions/1713335/peak-finding-algorithm-for-python-scipy

x = np.sin(2*np.pi*(2**np.linspace(2,10,1000))*np.arange(1000)/48000) + np.random.normal(0, 1, 1000) * 0.15
peaks, _ = find_peaks(x, distance=20)
peaks2, _ = find_peaks(x, prominence=1)      # BEST!
peaks3, _ = find_peaks(x, width=20)
peaks4, _ = find_peaks(x, threshold=0.4)     # Required vertical distance to its direct neighbouring samples, pretty useless
plt.subplot(2, 2, 1)
plt.plot(peaks, x[peaks], "xr"); plt.plot(x); plt.legend(['distance'])
plt.subplot(2, 2, 2)
plt.plot(peaks2, x[peaks2], "ob"); plt.plot(x); plt.legend(['prominence'])
plt.subplot(2, 2, 3)
plt.plot(peaks3, x[peaks3], "vg"); plt.plot(x); plt.legend(['width'])
plt.subplot(2, 2, 4)
plt.plot(peaks4, x[peaks4], "xk"); plt.plot(x); plt.legend(['threshold'])
plt.show()