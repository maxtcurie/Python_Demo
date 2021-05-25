import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

from FFT_general import FFT_function_time
from FFT_general import FFT_sum
from FFT_general import FFT_interp
from FFT_general import spectral_density
from FFT_general import spectral_density_sum
from FFT_general import spectral_density_interp
from FFT_general import test_functions
from FFT_general import time_average

#Created by Max Curie: 05/21/2021
#GitHub: https://github.com/maxcurie1996/Python_Demo/tree/main/FFT
frequency_all=True
frequency_min=0.
frequency_max=10.

function, time= test_functions(4)


plt.plot(time, abs(function))
plt.show()



f_FFT,amplitude_FFT,phase_FFT=\
    FFT_function_time(function,time,plot=False) 

sum_FFT,sum_error_FFT=\
    FFT_sum(f_FFT,amplitude_FFT,frequency_min,frequency_max,frequency_all)

f_den, Pxx_den= \
    spectral_density(function,time,percent=1.,window_for_FFT='hann',plot=False)

sum_den,sum_error_den=\
    spectral_density_sum(f_den,(Pxx_den)**0.5,frequency_min,frequency_max,frequency_all)

func_avg, func_std=\
    time_average(function,time)


print('**********************')
print('sum_FFT='+str(sum_FFT))
print('sum_den='+str(sum_den)) 
print('time_avg='+str(func_avg)+'+-'+str(func_std))
