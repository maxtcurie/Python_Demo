import numpy as np
import matplotlib.pyplot as plt


x=np.arange(0,6,0.001)
y1=np.sin(x)
y2=2.*np.cos(x)

Width=4*2
Height=3*2

plt.clf()

plt.figure(figsize=(Width,Height),dpi=96)

plt.plot(x,y1,label='sin')
plt.plot(x,y2,label='cos')
plt.xlim(-1,6)	#set the limit for the x axis
plt.ylim(-2,1.5)	#set the limit for the y axis
plt.xlabel(r'$x$',fontsize=10)
plt.ylabel(r'$sin(x)$',fontsize=10)
plt.title('Collisional Dependence',fontsize=20)
plt.legend()	#show the legend
plt.show()		#show the plot
plt.savefig('Output_plot.png')#save the 


