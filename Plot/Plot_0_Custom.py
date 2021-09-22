import numpy as np
import matplotlib.pyplot as plt

#Other good resources: https://youtu.be/UO98lJQ3QGI
#plot line style: https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.lines.Line2D.html#matplotlib.lines.Line2D.set_linestyle



x=np.arange(0,6,0.1)
y1=np.sin(x)
y2=2.*np.cos(x)

Width=4*2
Height=3*2

plt.clf()

plt.figure(figsize=(Width,Height),dpi=96)

plt.plot(x,y1,'r:',label='sin',alpha=0.2)   #red dot='r.', red line='r-', red dashline='r--'...
#alpha is transparency, 1 is sold, 0 is transparent
plt.plot(x,y2,'b:',label='cos')

#plt.xlim(-1,6)	#set the limit for the x axis
#plt.ylim(-2,1.5)	#set the limit for the y axis

#https://matplotlib.org/stable/api/matplotlib_configuration_api.html
#https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.gca.html
#https://stackoverflow.com/questions/21321670/how-to-change-fonts-in-matplotlib-python
#https://matplotlib.org/stable/tutorials/introductory/customizing.html
import matplotlib
fontname='Comic Sans MS'
font = {'family' : fontname,
        'weight' : 'bold',
        'size'   : 20}
matplotlib.rc('font', **font)

plt.xticks(**font)
plt.yticks(**font)
plt.xlabel('x lable',**font)
plt.ylabel('sin(x)',**font)
plt.title('Collisional Dependence',**font)

#vertical line
plt.axvline(1.,color='red',alpha=0.2)
#horizontal line
plt.axhline(1.,color='green',alpha=0.2)
plt.yscale("log") #log scale for y axis
plt.grid()
plt.legend()	#show the legend
plt.show()		#show the plot
plt.savefig('Output_plot.png')#save the 

