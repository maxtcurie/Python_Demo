import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Creating a sample time series data with missing values
np.random.seed(0)
dates = pd.date_range('20230101', periods=10)
data = np.random.randn(10)
data[3:6] = np.nan  # Introduce missing values

df = pd.Series(data, index=dates)

# Methods for backward-looking interpolation

# 1. Last Observation Carried Forward (LOCF)
locf = df.ffill()

# 2. Linear Interpolation (Backward)
linear_interp = df.interpolate(method='linear', limit_direction='backward')

# 3. Polynomial Interpolation (Backward)
# Using a simple linear polynomial as an example (degree = 1)
poly_interp = df.interpolate(method='polynomial', order=1, limit_direction='backward')

# 4. Exponential Smoothing
exp_smooth = df.ewm(span=3, adjust=False).mean()

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(df, marker='o', label='Original Data')
plt.plot(locf, marker='x', label='LOCF')
plt.plot(linear_interp, marker='v', label='Linear Interpolation')
plt.plot(poly_interp, marker='^', label='Polynomial Interpolation')
plt.plot(exp_smooth, marker='s', label='Exponential Smoothing')
plt.title('Comparison of Backward-Looking Interpolation Methods')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
