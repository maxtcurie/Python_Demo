import numpy as np
import matplotlib.pyplot as plt

#Other good resources: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.errorbar.html

marker_size=10	#size of the dot in the plot
x=np.arange(0,6,0.5)
x1_error=[0.5]*len(x)

y1=np.sin(x)
y1_error=y1*0.2

x2_error=[0.5]*len(x)
y2=2.*np.cos(x)
y2_error=y2*0.2

Width=4*2
Height=3*2

plt.clf()

plt.figure(figsize=(Width,Height),dpi=96)

plt.errorbar(x,y1,xerr=x1_error,yerr=y1_error,marker='s',ms=marker_size,linestyle='none',label='sin')   
plt.errorbar(x,y2,xerr=x2_error,yerr=y2_error,marker='o',ms=marker_size,linestyle='none',label='cos')
plt.xlim(-1,6)	#set the limit for the x axis
plt.ylim(-2,1.5)	#set the limit for the y axis
plt.xlabel(r'$x$',fontsize=10)
plt.ylabel(r'$sin(x)$',fontsize=10)
plt.title('Collisional Dependence',fontsize=20)
plt.legend()	#show the legend
plt.show()		#show the plot
plt.savefig('Output_plot.png')#save the 

