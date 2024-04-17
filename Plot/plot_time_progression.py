import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np 
n_start=1
n_end=10

t=np.arange(0,6,0.01)

index=np.arange(n_start, n_end, 1, dtype=int)

plot_=np.sin(t)

colors = cm.jet(np.linspace(0, 1, len(index)))

#Profile
plt.clf()
for idx, i in enumerate(index):
    plt.plot(np.sin(t)*i, color=colors[idx])
    
plt.xlabel('t',fontsize=20)
plt.ylabel('n*sin(t)',fontsize=20)
plt.show()