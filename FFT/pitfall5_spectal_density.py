import matplotlib.pyplot as plt
import numpy as np
from spectral_density import spectral_density
from FFT_general import FFT_sum
from FFT_general import sort_x_f
from Test_functions import test_functions

function, time=test_functions(function_num=3)

frequency_sort,amplitude_frequency_sort,phase_frequency_sort=spectral_density(function,time,percent=0.5,window_for_FFT='boxcar',plot=False)

frequency_min=np.min(frequency_sort)
frequency_max=np.max(frequency_sort)
frequency_all=True

sum0,sum0_error=FFT_sum(frequency_sort,amplitude_frequency_sort,frequency_min,frequency_max,frequency_all)
print('sum0,sum0_error='+str(sum0)+', '+str(sum0_error))

total_len_scale=1.5
uni_frequency_sort=np.linspace(np.min(frequency_sort),np.max(frequency_sort),int(len(frequency_sort)*total_len_scale))
uni_amplitude_frequency_sort=np.interp(uni_frequency_sort,frequency_sort,amplitude_frequency_sort)

print('After interpolation without the factor')
sum0,sum0_error=FFT_sum(uni_frequency_sort,uni_amplitude_frequency_sort,frequency_min,frequency_max,frequency_all)
print('sum0,sum0_error='+str(sum0)+', '+str(sum0_error))

uni_amplitude_frequency_scaled=uni_amplitude_frequency_sort*float(len(frequency_sort))/float(len(uni_frequency_sort))

print('After multiply the factor'+str(float(len(frequency_sort))/float(len(uni_frequency_sort))))
sum0,sum0_error=FFT_sum(uni_frequency_sort,uni_amplitude_frequency_scaled,frequency_min,frequency_max,frequency_all)
print('sum0,sum0_error='+str(sum0)+', '+str(sum0_error))


plt.clf()
plt.plot(frequency_sort,amplitude_frequency_sort,label='Original')
plt.plot(uni_frequency_sort,uni_amplitude_frequency_sort,label='interpolation without scale')
plt.plot(uni_frequency_sort,uni_amplitude_frequency_scaled,label='interpolation with scale')
plt.legend()
plt.show()