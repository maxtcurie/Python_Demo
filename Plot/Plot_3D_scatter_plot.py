import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Sample data - replace this with your df_para
np.random.seed(0)
df_para = pd.DataFrame({
    'Te_list': np.random.rand(100),
    'Ti_list': np.random.rand(100),
    'ne_list': np.random.rand(100)
})

# Your specified parameters
marker_size = 10
fontsize0 = 10

# Clear the current figure
plt.clf()

# Create a figure
fig = plt.figure()

# Create a 3D axis
ax = fig.add_subplot(111, projection='3d')

# Create a scatter plot
scatter = ax.scatter(df_para['Te_list'], df_para['Ti_list'], df_para['ne_list'], 
                     c='gray', s=marker_size, label='Path to success')

# Set labels
ax.set_xlabel('Te', fontsize=fontsize0)
ax.set_ylabel('Ti', fontsize=fontsize0)
ax.set_zlabel('ne', fontsize=fontsize0)

# Remove tick labels
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

# Add legend
plt.legend()

# Show the plot
plt.show()
