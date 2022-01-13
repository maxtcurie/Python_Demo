import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import ConnectionPatch
#https://towardsdatascience.com/5-powerful-tricks-to-visualize-your-data-with-matplotlib-16bc33747e05

x=np.arange(0,6,0.0001)
y=np.sin(x)*np.sin(100.*x)

#Full plot
xmin1, xmax1, ymin1, ymax1=0,6,-2,2
#Zoom plot
xmin2, xmax2, ymin2, ymax2=1,2,-1.5,1.5

# Create main container with size of 6x5
fig = plt.figure(figsize=(12, 6))
#plt.subplots_adjust(bottom = 0.1, left = 0.1, top =0.9, right = 0.9)

# Create first axes, the top-left plot with green plot
sub1 = fig.add_subplot(1,2,1) # two rows, two columns, fist cell
sub1.plot(x, y, color = 'blue')
sub1.set_xlim(xmin1, xmax1)
sub1.set_ylim(ymin1, ymax1)
sub1.set_ylabel('y', labelpad = 15)
sub1.set_xlabel('x', labelpad = 15)

# Create second axes, the top-left plot with orange plot
sub2 = fig.add_subplot(1,2,2) # two rows, two columns, second cell
sub2.plot(x, y, color = 'orange')
sub2.set_xlim(xmin2, xmax2)
sub2.set_ylim(ymin2, ymax2)
sub2.set_xlabel('x', labelpad = 15)

# Create blocked area in third axes
x_fill=[xmin2,xmin2,xmax2,xmax2]
y_fill=[ymin2,ymax2,ymax2,ymin2]
sub1.fill(x_fill,y_fill,color='green',alpha=0.6,label='highlight')
# Create bottom side of Connection patch for first axes
con1 = ConnectionPatch(xyA=(xmax2, ymin2), coordsA=sub1.transData, 
                       xyB=(xmin2, ymin2), coordsB=sub2.transData, color = 'green')
# Add bottom side to the figures
fig.add_artist(con1)

# Create upper side of Connection patch for first axes
con2 = ConnectionPatch(xyA=(xmax2, ymax2), coordsA=sub1.transData, 
                       xyB=(xmin2, ymax2), coordsB=sub2.transData, color = 'green')
# Add upper side to the figure
fig.add_artist(con2)

plt.show()
# Save figure with nice margin
#plt.savefig('zoom_effect_2.png', dpi = 300, bbox_inches = 'tight', pad_inches = .1)