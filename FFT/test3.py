from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from Spectral_density import spectral_density
from FFT_general import FFT_function_time
import cmath

fs = 10e3
N = 1e4




omega=20.


number=-2.-1.j
a=np.power(number,2.,dtype=complex)
a=np.power(a,0.5,dtype=complex)
#a=number**2.
print('a='+str(a))

time = np.arange(N) / fs
function = np.exp(-1.j * omega * time -3.j)+0.5*np.exp(+1.j * 2*omega * time-1.j)

plt.clf()
#plt.plot(time,function)
plt.plot(time,np.real(function),label='real')
plt.plot(time,np.imag(function),label='imag')
plt.title('function')
plt.legend()
plt.show()

function = np.power(function,2.,dtype=complex)
function = np.power(function,0.5,dtype=complex)

plt.clf()
#plt.plot(time,function)
plt.plot(time,np.real(function),label='real')
plt.plot(time,np.imag(function),label='imag')
plt.title('((function)**2.)**0.5')
plt.legend()
plt.show()

f, Pxx_den=spectral_density(function,time,window_for_FFT='boxcar',plot=False)
frequency_sort,amplitude_frequency_sort,phase_frequency_sort=FFT_function_time(function,time,plot=False)


#f, Pxx_den = signal.periodogram(function, fs)

#plt.semilogy(f, Pxx_den)
plt.plot(f, np.sqrt(Pxx_den),label='Welch')
plt.plot(frequency_sort,amplitude_frequency_sort,label='FFT')
plt.ylim([1e-7, 1e2])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.legend()
plt.show()