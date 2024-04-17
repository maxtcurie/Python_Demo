import numpy as np

# Simulating a 3D array with `nan` values
array = np.random.rand(10, 5, 3)
array[2, 2, 1] = np.nan
array[4, 3, 2] = np.nan

# Filter out samples that contain any `nan` values
filtered_array = array[~np.any(np.isnan(array), axis=(1, 2))]

print("Original shape:", array.shape)
print("Filtered shape:", filtered_array.shape)
