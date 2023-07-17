import numpy as np

# Example 1D array
input_array = np.array([1, 2, 3, 4, 5])

# Desired length after padding
desired_length = 8

# Padding the array
padded_array = np.pad(input_array, (0, desired_length - len(input_array)), mode='constant')

print("Padded Array:", padded_array)


padded_array = np.pad(input_array, (desired_length - len(input_array), 0), mode='constant')

print("Padded Array:", padded_array)
