import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np 

psin=np.linspace(0,1,100)
index=np.arange(0,20,1, dtype=int)

colors = cm.jet(np.linspace(0, 1, len(index)))

#Profile
plt.clf()
for idx, i in enumerate(index):
    plt.plot(psin,psin*idx*0.1, color=colors[idx], alpha=0.4)
    
plt.xlabel(r'$\psi_n$',fontsize=20)
plt.ylabel('psin*idx',fontsize=20)
plt.show()