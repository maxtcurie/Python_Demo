import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def generate_sine_data_with_nans(num_points=1000, nan_ratio=0.1):
    time = np.linspace(0, 10 * np.pi, num_points)
    data = np.sin(time)
    nan_indices = np.random.choice(num_points, int(num_points * nan_ratio), replace=False)
    data[nan_indices] = np.nan
    return time, data

def interpolate_and_fill(time, data, new_time, fill):
    valid_mask = ~np.isnan(data)
    valid_time = time[valid_mask]
    valid_data = data[valid_mask]

    interp_func = interp1d(valid_time, valid_data, kind=fill, bounds_error=False, fill_value="extrapolate")
    return interp_func(new_time)

# Extend time domain for demonstration
time, data = generate_sine_data_with_nans(num_points=1000, nan_ratio=0.1)
extended_time = np.linspace(-2, 10 * np.pi + 2, 1200)  # Extended time array

# Applying the interpolation functions
filled_data_backward = interpolate_and_fill(time, data, extended_time, "previous")
filled_data_linear = interpolate_and_fill(time, data, extended_time, "linear")

# Plotting the results
plt.figure(figsize=(14, 7))
plt.plot(time, data, 'o', label='Original Data', color='gray', alpha=0.3)
plt.plot(extended_time, filled_data_backward, label='Backward Fill Extrapolated', color='red')
plt.plot(extended_time, filled_data_linear, label='Linear Interpolation Extrapolated', color='blue')
plt.title('Extrapolation of Interpolation Methods on Sine Wave with Missing Data')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()
