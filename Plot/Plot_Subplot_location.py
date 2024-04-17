import matplotlib.pyplot as plt

# Create a figure
fig = plt.figure(figsize=(10, 6))

# Create the first subplot at the top left (1, 2, 1) means 1 row, 2 cols, position 1
ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title('Subplot 1')
ax1.plot([0, 1], [0, 1])  # Simple plot for demonstration

# Create the second subplot at the top right (1, 2, 2) means 1 row, 2 cols, position 2
ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title('Subplot 2')
ax2.plot([0, 1], [1, 0])  # Another simple plot for demonstration

# Create the third subplot that spans the bottom row
# (2, 1, 3) means 2 rows, 1 col, position 3, but it starts counting in row-major order
ax3 = fig.add_subplot(2, 1, 2)
ax3.set_title('Subplot 3')
ax3.plot([1, 0], [0, 1])  # Yet another simple plot

plt.tight_layout()  # Adjust subplots to fit into the figure area.
plt.show()  # Display the plots
