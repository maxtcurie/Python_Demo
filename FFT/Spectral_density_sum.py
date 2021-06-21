import numpy as np
import matplotlib.pyplot as plt
from FFT_general import spectral_density_sum
from FFT_general import spectral_density_interp

def gaussian_max(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / (1.*stddev))**2.)

freq=np.arange(0,100,0.01)
amp_sq=gaussian_max(freq, 1., 50., 20.)**2.

sum0,sum0_error=\
    spectral_density_sum(freq,amp_sq**0.5,0,100.,frequency_all=True)


uni_frequency_sort,uni_amplitude_frequency_sort=\
    spectral_density_interp(freq,amp_sq**0.5,total_len_scale=10.)

sum0_interp,sum0_error=\
    spectral_density_sum(uni_frequency_sort,uni_amplitude_frequency_sort,0,100.,frequency_all=True)


print('sum0       = '+str(sum0))
print('sum0_interp= '+str(sum0_interp))