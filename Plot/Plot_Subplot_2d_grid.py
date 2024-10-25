import matplotlib.pyplot as plt
import numpy as np

# Example plotting function
def plot_example(ax, data, index):
    ax.plot(data)
    ax.set_title(f'Plot {index+1}')

def plot_grid(plot_function, data, figsize=(15, 10)):
    """
    Creates a grid of subplots.

    Parameters:
    n (int): Total number of subplots.
    plot_function (function): A function that takes an axis, data, and index to plot in each subplot.
    data (list): List of data to plot, one per subplot.
    figsize (tuple): Size of the entire figure.
    """
    n=len(data)
    # Calculate number of rows and columns
    rows = int(n**0.5)
    cols = n // rows + 1
    
    # Create subplots
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    
    # Flatten axes for easy indexing
    axes = axes.flatten()

    # Plot each subplot
    for i in range(n):
        plot_function(axes[i], data[i], i)

    # Remove empty subplots if there are any
    for i in range(n, rows * cols):
        fig.delaxes(axes[i])

    plt.tight_layout()
    plt.show()


# Example usage
n = 10
data = [np.random.rand(10) for _ in range(n)]
plot_grid(plot_example, data)
