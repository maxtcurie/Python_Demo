import numpy as np
import matplotlib.pyplot as plt
#two coordinate mapping arry: rho, psi
#the function y_rho2=y(rho2)
#one want to get: y_psi2

rho=np.arange(0,1.00000001,0.001)
psi=rho**0.5 #the translation between x and x2, but the coordinate will still be x

rho2=np.arange(0,1.00000001,0.0001)
y_rho2=np.sin(10.*rho2)


#example: np.interp(new_x, x, y)
 
#getting the 
psi2=np.interp(rho2,rho,psi)
y_psi2=np.interp(psi2,rho2,y_rho2)

plt.clf()
plt.plot(psi2,y_psi2,label='y_psi')
plt.plot(rho2,y_rho2,label='y_rho')
plt.legend()
plt.show()