import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#Exp_data=pd.read_csv('Experiment.csv')  
#Sim_data=pd.read_csv('Simulation.csv')  
GL_MTM=pd.read_csv('MTM_GL_gamma.csv')  
GL_other=pd.read_csv('Other_GL_gamma.csv')
Mode_finder=pd.read_csv('MTM_dispersion_n_scan_tracor_profile.csv')
#print(Exp_data)
#print(type(Exp_data))
#plt.errorbar(trip.index, trip.gas, yerr=trip.std)

plt.clf()
#plt.figure()
#plt.figure(
#    figsize=(4*(np.max(outer_R)-np.min(outer_R)), 4*(np.max(outer_Z)-np.min(outer_Z))),
#    dpi=96)
#fig,ax1 = plt.subplots()
ymax=0.25
ax2=Mode_finder.plot(kind='scatter',x='n',y='gamma(cs/a)',style='o',ylim=(0.00,ymax),s=50,color='red',grid=True,label='Mode finder')
GL_MTM.plot(kind='scatter',x='n',y='gamma',style='o',s=50,color='blue',ylim=(0.00,ymax),grid=True,label='Simulation MTM',ax=ax2)
GL_other.plot(kind='scatter',x='n',y='gamma',style='o',s=50,color='grey',ylim=(0.00,ymax),grid=True,label='Simulation Other',ax=ax2)

ax2.set_xlabel('Toroidal mode number',fontsize=15)
ax2.set_ylabel(r'$\gamma(cs/a)$',fontsize=15)
#plt.xlim(1.0,1.3)

#ax2.ylim(0,1)

#plt.legend()
#plt.ylabel(r'$\bar{B}_r$',fontsize=10)
#plt.xlabel(r'$\frac{\nu_{ei}}{\omega}$',fontsize=10)
#plt.plot(data.,Z_in)
#plt.title('Collisional Dependence',fontsize=20)
plt.show()
#plt.savefig('nu_scan.png')

'''
# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)')
ax1.set_ylabel('exp', color=color)
ax1.plot(t, data1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
ax2.plot(t, data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
'''