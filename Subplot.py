import numpy as np
from astropy import modeling
import matplotlib.pyplot as plt
from scipy import optimize


np.set_printoptions(precision=2)
a=0.1230265431
fontsize0=12
print(a)

#subplot
#refers to https://youtu.be/XFZRVnP-MTU
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
#for i in range(2):
#	for j in range(2):
#		ax[i,j].legend()

plt.tight_layout()
plt.show()