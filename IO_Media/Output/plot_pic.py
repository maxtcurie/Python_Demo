import numpy as np
import matplotlib.pyplot as plt


image_path = './'

x=np.arange(0,7,0.001)
for i in range(10):
    plt.clf()
    plt.plot(x,x*float(i),label='y='+str(i)+'*x')
    plt.ylim(0,10)
    plt.grid()
    plt.legend()
    plt.savefig(image_path+str(i)+'.png')

    plt.clf()
    plt.plot(x,np.sin(x)*float(i),label='y='+str(i)+'*sin(x)')
    plt.ylim(-15,15)
    plt.grid()
    plt.legend()
    plt.savefig(image_path+str(i)+'_sin.png')