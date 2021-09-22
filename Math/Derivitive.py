import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,6,0.1)
y1=np.sin(x)

#Derivative
dy1= np.gradient(y1,x)

plt.clf()
plt.plot(x,y1,'r:',label='y1',alpha=0.2)   
plt.plot(x,dy1,'b:',label='dy1',alpha=0.2)   
plt.grid()
plt.legend()	
plt.show()		

