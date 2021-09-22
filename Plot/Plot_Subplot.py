import numpy as np
import matplotlib.pyplot as plt


fontsize0=12

#subplot
#refers to https://youtu.be/XFZRVnP-MTU
#https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.subplot.html
x=np.arange(0,6,0.001)
fig, ax=plt.subplots(nrows=2,ncols=2,sharex=True) 
			#nrows is the total rows
			#ncols is the total columns
			#sharex true means the xaxies will be shared
ax[0,0].plot(x,np.sin(x),label='sin(x)')
#ax[0,0].set_xlabel('x')
ax[0,0].set_ylabel('sin(x)',fontsize=fontsize0)
#ax1.set_title()		#for the set the title name
ax[0,1].plot(x,np.cos(x),label='cos(x)')
#ax[0,1].set_xlabel('x')
ax[0,1].set_ylabel('cos(x)',fontsize=fontsize0)
ax[1,0].plot(x,np.sin(x)**2.,label='sin(x)^2')
ax[1,0].set_xlabel('x',fontsize=fontsize0)
ax[1,0].set_ylabel('sin(x)^2',fontsize=fontsize0)
ax[1,1].plot(x,np.cos(x)**2.,label='cos(x)^2')
ax[1,1].set_xlabel('x',fontsize=fontsize0)
ax[1,1].set_ylabel('cos(x)^2',fontsize=fontsize0)
ax[1,1].set_xlim([0, 5])
#for i in range(2):
#	for j in range(2):
#		ax[i,j].legend()

#for no space between plots: https://stackoverflow.com/questions/20057260/how-to-remove-gaps-between-subplots-in-matplotlib/45487279
#plt.subplots_adjust(wspace=0, hspace=0)

plt.tight_layout()
plt.show()