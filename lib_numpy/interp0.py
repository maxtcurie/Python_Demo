import numpy as np

#interp 1D array
x=np.arange(0,6.00001,0.001)
y=np.sin(x)

x2=np.arange(0,6.00001,0.0002)
y2=np.interp(x2,x,y)

import matplotlib.pyplot as plt

plt.clf()
plt.plot(x,y,  label='original')
plt.plot(x2,y2,label='interp')
plt.legend()
plt.show()

#interp 2D array
x=np.arange(1,6,0.5)
y=np.arange(0,6.00001,0.001)
z=np.outer(x,np.sin(y))

x2=np.arange(0,5.0001,0.3)
y2=np.arange(0,6.00001,0.0002)


def interp_2D(z,x,y,x2,y2,plot=False): #for z(x,y)
	(nx,ny)=np.shape(z)
	z_tmp=np.zeros((nx,len(y2)))
	for i in range(nx):
		z_tmp[i,:]=np.interp(y2,y,z[i,:])

	z2=np.zeros((len(x2),len(y2)))
	for i in range(len(y2)):
		z2[:,i]=np.interp(x2,x,z_tmp[:,i])
	if plot:
		plt.clf()
		plt.plot(y,z[0,:],label='original',alpha=0.1)
		plt.plot(y2,z2[0,:],label='interp',alpha=0.1)
		for i in range(len(x)):
			plt.plot(y,z[i,:],alpha=0.1)
		for i in range(len(x2)):
			plt.plot(y2,z2[i,:],alpha=0.6)
		plt.legend()
		plt.show()
	return z2

z2=interp_2D(z,x,y,x2,y2,plot=True)


