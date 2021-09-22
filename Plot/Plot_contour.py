import numpy as np
import matplotlib.pyplot as plt

name='sin(x)cos(y)'

x=np.arange(0,6,0.001)
y=np.arange(0,6,0.001)
z=np.outer(np.sin(x),np.cos(y))

plt.clf()
plt.ylabel(r'$k_y \rho_s$',fontsize=10)
plt.xlabel(r'$f(kHz)$',fontsize=10)
plt.contourf(x,y,z)#,level=[50,50,50])#,cmap='RdGy')

#plt.axhline(ky_list[0],color='red',alpha=0.5,label='n starts from'+str(n_list[0]) )#alpha control the transparency, alpha=0 transparency, alpha=1 solid
#plt.legend()
plt.colorbar()
plt.title(str(name)+' contour plot',fontsize=10)
#plt.savefig(pic_path+'/'+str(name)+'_log_contour_plot.png')

plt.show()