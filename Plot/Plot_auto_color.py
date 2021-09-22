import numpy as np
import matplotlib.pyplot as plt

#Other good resources: https://youtu.be/UO98lJQ3QGI
#plot line style: https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle


total_band_num=10
x=np.arange(0,6,0.1)
#y1=np.sin(x)
#y2=2.*np.cos(x)


color_list=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

plt.clf()
plt.plot()
for i in range(total_band_num):
	plt.plot(x,float(i)*np.sin(x),color=color_list[i%len(color_list)],label='band '+str(i))
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('title',fontsize=20)
plt.show()
#plt.savefig('Output_plot.png')#save the 
