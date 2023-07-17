import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# Generate example data
x = np.random.rand(1000)
y = np.random.rand(1000)
z = np.sin(x * np.pi) * np.cos(y * np.pi)

# Define the coordinates for interpolation
xi = np.linspace(0, 1, 1000)
yi = np.linspace(0, 1, 1000)

# Create a meshgrid of the coordinates
xi, yi = np.meshgrid(xi, yi)

# Perform interpolation
zi = griddata((x, y), z, (xi, yi), method='linear')

# Create a figure and axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Plot the original data
ax1.scatter(x, y, c=z, cmap='viridis')
ax1.set_title('Original Data')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

# Plot the interpolated data
im = ax2.imshow(zi, origin='lower', extent=(0, 1, 0, 1), cmap='viridis')
ax2.set_title('Interpolated Data')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
plt.colorbar(im)

# Adjust the layout and display the plot
plt.tight_layout()
plt.show()
