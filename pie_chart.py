import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Exp_data=pd.read_csv('Experiment.csv')  
#Sim_data=pd.read_csv('Simulation.csv')  
#data=pd.read_csv('Theory3.csv')  


plt.clf()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'MTM', 'ETG', 'Neoclassical'#, 'Other'

sizes = [2.7, 0.17, 0]
neo=4.2-np.sum(sizes)
sizes = [0.52, 0.17, neo]
sizes=sizes/np.sum(sizes)
explode = (0.1, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

#plt.savefig('nu_scan.png')
