from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import numpy as np
#https://stackoverflow.com/questions/20618804/how-to-smooth-a-curve-in-the-right-way

x = np.linspace(0,2*np.pi,30)
y = np.sin(x) + np.random.random(30) * 0.2

def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

y2=smooth(y, 5)
y3=savgol_filter(y, 5, 2)

plt.scatter(x,y,alpha=0.6)
plt.plot(x,y2,label='y2')
plt.plot(x,y3,label='y3')
plt.legend()
plt.show()
