import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d

#Other good resources: https://youtu.be/UO98lJQ3QGI
#plot 3D: https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html

fig = plt.figure()
ax = plt.axes(projection='3d')



a=2.
b=3.
marker_size=10
fontsize0=10

plt.clf()
fig = plt.figure()

ax = plt.axes(projection='3d')

# Data for a three-dimensional line
zline = np.linspace(0, 15, 1000)
xline = b*zline*np.sin(a*zline)
yline = b*zline*np.cos(a*zline)
ax.plot3D(xline, yline, zline, 'gray',label='Path to success')
ax.plot([xline[200]], [yline[200]], [zline[200]],'red',marker='o',ms=marker_size,label='You')
ax.set_xlabel('Oppertunity',fontsize=fontsize0)
ax.set_ylabel('Skill',fontsize=fontsize0)
ax.set_zlabel('Effort',fontsize=fontsize0)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])
plt.legend()

plt.show()

'''
# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
'''


