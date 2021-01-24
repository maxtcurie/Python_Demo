import numpy as np
import matplotlib.pyplot as plt

#https://numpy.org/doc/stable/reference/generated/numpy.interp.html
x=np.arange(0,6,0.01)	#creating the array from 0 to 6 with step of 0.01
f=np.sin(x)				#f=sin(x)
new_x=np.arange(0,6,0.001)	#creating the array from 0 to 6 with step of 0.001
new_f=np.interp(new_x,x,f)	#Interprolate f with new_x 
plt.clf()
plt.plot(x,f,label='original')
plt.plot(new_x,new_f,label='interp, 10time')
new_x=np.arange(0,6,0.5)	#creating the array from 0 to 6 with step of 0.5
new_f=np.interp(new_x,x,f)	#Interprolate f with new_x 
plt.plot(new_x,new_f,label='interp, 0.02time')
plt.legend()
plt.show()
