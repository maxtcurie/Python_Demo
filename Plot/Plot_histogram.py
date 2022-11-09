#https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
x = np.random.normal(size=1000)

plt.clf()
plt.hist(x, density=True, bins=30)  # density=False would make counts
plt.ylabel('Probability')
plt.xlabel('Data');
plt.show()