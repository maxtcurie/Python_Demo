import numpy as np
import math
import matplotlib.pyplot as plt

def create_line_filter(size, angle_degrees):
    # Create a basic horizontal line filter
    filter_matrix = np.zeros((size, size))
    filter_matrix[size // 2, :] = 1

    # Calculate the rotation angle in radians
    angle_radians = math.radians(angle_degrees)

    # Create rotation matrix
    cos_a, sin_a = math.cos(angle_radians), math.sin(angle_radians)
    rotation_matrix = np.array([[cos_a, -sin_a], [sin_a, cos_a]])

    # Rotate each point in the filter matrix
    center = size // 2
    for x in range(size):
        for y in range(size):
            # Shift to origin, rotate, and shift back
            dx, dy = x - center, y - center
            new_dx, new_dy = np.dot(rotation_matrix, [dx, dy])
            new_x, new_y = new_dx + center, new_dy + center

            # Use nearest neighbor interpolation for rotated positions
            if int(round(new_x)) == center and 0 <= int(round(new_y)) < size:
                filter_matrix[x, y] = 1
            else:
                filter_matrix[x, y] = -1

    return filter_matrix

# Example usage
size = 10  # Size of the filter matrix
angle = 30  # Angle in degrees
line_filter = create_line_filter(size, angle)

# Plotting the filter matrix
plt.imshow(line_filter, cmap='gray', interpolation='nearest', aspect='equal')
plt.colorbar()
plt.title(f'Line Filter Matrix at {angle} Degrees')
plt.show()