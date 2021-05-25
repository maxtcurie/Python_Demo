from FFT_general import FFT_function_time
from FFT_general import FFT_sum
from FFT_general import FFT_interp
from FFT_general import spectral_density
from FFT_general import spectral_density_sum
from FFT_general import spectral_density_interp
from FFT_general import test_functions
from FFT_general import time_average

#Video about Pitfalls in FFT: https://youtu.be/jZVekQ2ZDXQ

#**********************************************
# this function does FFT(Fast Fourier transform) for function of time (uniform or ununiform)
# input the function of time array, time(array), plot(True if on wants to the plot the g(freq))
frequency_sort,amplitude_frequency_sort,phase_frequency_sort=\
    FFT_function_time(function,time,plot=False) 
# output the frequency that is monotonic increasing, amplitude(freq), phase(freq)
#**********************************************

#**********************************************
# this fucntion sum the amplitude from the output of FFT
# input the frequency, amplitude(freq), 
#           lower bound of frequency to be sum, 
#           upper bound of frequency to be sum, 
#           Change to True if one wants to sum over the full frequency
sum0,sum0_error=
    FFT_sum(f,amp_f,frequency_min,frequency_max,frequency_all)
# output is the sum(float), sum0_error(float, 0. for now)
#**********************************************

#**********************************************
# this function interpolate the frequency,amplitude_frequency in the correct way with the scaling factor
# input is the frequency, amplitude(freq), len(uni_frequency_sort) = len(frequency)*total_len_scale
uni_frequency_sort,uni_amplitude_frequency_sort=\
    FFT_interp(frequency,amplitude_frequency,total_len_scale=1.5)
# output is the interpoplated the frequency, amplitude(freq)
#**********************************************

#**********************************************
# this fucntion sum the amplitude from the output of spectral density
# input the function of time array, time(array), plot(True if on wants to the plot the g(freq))
f, Pxx_den=
    spectral_density(function,time,percent=0.5,window_for_FFT='hann',plot=False)
# output the frequency that is monotonic increasing, [ amplitude^2/(Time) ] (freq)
#**********************************************

#**********************************************
# this fucntion sum the amplitude from the output of spectral density
# input the frequency, amplitude(freq)/unit[ amp/(Hz)^0.5 ], 
#           lower bound of frequency to be sum, 
#           upper bound of frequency to be sum, 
#           Change to True if one wants to sum over the full frequency
sum0,sum0_error=\
    spectral_density_sum(f,amp_f,frequency_min,frequency_max,frequency_all)
# output is the sum(float), sum0_error(float, 0. for now)
#**********************************************

#**********************************************
# this function interpolate the frequency,amplitude_frequency in the correct way with the scaling factor
# input is the frequency, amplitude(freq), len(uni_frequency_sort) = len(frequency)*total_len_scale
uni_frequency_sort,uni_amplitude_frequency_sort=\
    spectral_density_interp(frequency,amplitude_frequency,total_len_scale=1.5)
# output is the interpoplated the frequency, amplitude(freq)
#**********************************************

#**********************************************
# this provides the test functions
# input number(int) from 1-3
function, time=\
    test_functions(function_num=1)
#output test_functions(1): 3.*np.sin(2*np.pi*1000.*time)+noise
#       test_functions(2): 1+np.exp(-1.j * omega * time -3.j)+0.5*np.exp(+1.j * 2*omega * time-1.j), where omega=2.*np.pi*200
#       test_functions(3): g(freq) is gaussian centered around 200
#**********************************************

#**********************************************
func_avg, func_std=\
    time_average(function,time)
#**********************************************