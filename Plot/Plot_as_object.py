import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def plot_as_obj():
    x=np.arange(0,6,0.01)
    fig, ax = plt.subplots()
    ax.plot(x,np.sin(x),label=r'Safety factor $q_0$')
    return fig, ax 

fig1, ax1=plot_as_obj()
plt.show()
