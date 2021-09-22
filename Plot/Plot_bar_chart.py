import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

#https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.bar.html
width=0.5
labels = ['1', '2']
#colors=['orange','blue']
sizes = [2.37, 0.17]#, 0]	
error = [0.32,0.01]#,0]

total_trans=2.1
trans_error=0.5
#neo=total_trans-np.sum(sizes)

locations=np.arange(0.5*width,0.5*width+float(len(labels))*width+0.00001,width)
x_max=np.max(locations+0.5*width)
x=[0,0,x_max,x_max]
y=[total_trans-trans_error,total_trans+trans_error,total_trans+trans_error,total_trans-trans_error]
total=np.sum(sizes)
total_error=0
for i in error:
	total_error=total_error+i**2.

total_error=np.sqrt(total_error)

plt.clf()
matplotlib.patches.Rectangle((0,total_trans-trans_error),10,2.*trans_error,alpha=0.4)

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
for i in range(len(sizes)):
	plt.bar(locations[i], sizes[i], width, yerr=error[i],label=labels[i])

plt.bar(locations[-1], total, width, yerr=total_error,label='total')

#plt.axhline(total_trans,color='red',alpha=0.5,label='total transport')
#plt.xlabel(r'$x$',fontsize=10)
plt.fill(x,y,alpha=0.6,label='total transport')
plt.ylabel('Power(MW)',fontsize=10)
plt.legend()

plt.show()

