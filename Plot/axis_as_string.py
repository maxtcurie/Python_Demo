import numpy as np
import matplotlib.pyplot as plt

#from: https://stackoverflow.com/questions/3100985/plot-with-custom-text-for-x-axis-points

total_band_num=10
x=np.arange(0,6,0.1)

plt.clf()
plt.plot()
plt.plot(x,np.sin(x))

x=np.arange(4)
my_xticks = ['John','Arnold','Mavis','Matt']
plt.xticks(x, my_xticks,rotation=45)

plt.ylabel('y')
plt.title('title',fontsize=20)
plt.show()
#plt.savefig('Output_plot.png')#save the 
