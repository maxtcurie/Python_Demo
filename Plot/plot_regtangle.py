#from: https://www.statology.org/matplotlib-rectangle/
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

bottom_left_coord=(1,0)

width=2
height=1


#define Matplotlib figure and axis
fig, ax = plt.subplots()

#create simple line plot
ax.plot([0, 10],[0, 10])

#add rectangle to plot
ax.add_patch(Rectangle(bottom_left_coord, width,height, linewidth=1, edgecolor='r', facecolor='none'))

#display plot
plt.show()