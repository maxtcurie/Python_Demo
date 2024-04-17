import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def generate_sine_data_with_nans(num_points=1000, nan_ratio=0.1):
    """ Generate sine wave data with random NaNs inserted. """
    time = np.linspace(0, 10*np.pi, num_points)
    data = np.sin(time)
    nan_indices = np.random.choice(num_points, int(num_points * nan_ratio), replace=False)
    data[nan_indices] = np.nan
    return time, data

def interpolate_and_fill(time, data, fill="backward"):
    """ Interpolate and fill data using Scipy. """
    valid_mask = ~np.isnan(data)
    valid_time = time[valid_mask]
    valid_data = data[valid_mask]

    if fill == "backward":
        interp_func = interp1d(valid_time, valid_data, kind='previous', bounds_error=False, fill_value="extrapolate")
    elif fill == "linear":
        interp_func = interp1d(valid_time, valid_data, kind='linear', bounds_error=False, fill_value="extrapolate")
    
    filled_data = interp_func(time)
    return filled_data

# Generate data
num_points = 1000
nan_ratio = 0.1
time, data = generate_sine_data_with_nans(num_points, nan_ratio)

# Interpolate data
filled_data_backward = interpolate_and_fill(time, data, fill="backward")
filled_data_linear = interpolate_and_fill(time, data, fill="linear")

# Plotting the results
plt.figure(figsize=(14, 7))
plt.plot(time, data, label='Original Data', color='gray', linestyle='--', marker='', alpha=0.5)
plt.plot(time, filled_data_backward, label='Backward Fill', color='red', linestyle='-', marker='',alpha=0.3)
plt.plot(time, filled_data_linear, label='Linear Interpolation', color='blue', linestyle='-', marker='',alpha=0.1)
plt.title('Comparison of Interpolation Methods on Sine Wave with Missing Data')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
