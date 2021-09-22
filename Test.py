import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

f_min=10
f_max=130

plt.plot(np.arange(0,1.2,(1.2/1000)),[f_min]*1000, color="purple", label='Frequency boundary')
plt.axhline(f_max, color="purple")
plt.show()