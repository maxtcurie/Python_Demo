from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from Spectral_density import spectral_density
from FFT_general import FFT_function_time
import cmath

def gaussian_max(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / (1.*stddev))**2.)

def test_functions(function_num=1):
    fs = 10e3
    N = 1e5
    
    time = np.arange(N) / fs
    if function_num==1:
        amp = 2*np.sqrt(2)
        freq = 1234.0
        np.random.seed(1234)
        noise_power = 0.001 * fs / 2
        function = amp*np.sin(2*np.pi*freq*time)
        function += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)

    elif function_num==2: 
        omega=2.*np.pi*200
        function=1+np.exp(-1.j * omega * time -3.j)+0.5*np.exp(+1.j * 2*omega * time-1.j)

    elif function_num==3:
        omega=2.*np.pi*200
        omega_list=np.arange(omega*0.2,omega*1.9,0.1)
        x_list=np.linspace(-2,2,len(omega_list))
        mode_list=gaussian_max(x_list, 1, 0, 0.5)
        for i in range(len(omega_list)):
            omega=omega_list[i]
            mode = mode_list[i]
            if i==0:
                function = mode*np.exp(-1.j * omega * time )
            else:
                function += mode*np.exp(-1.j * omega * time )
    if 0==1:
        plt.clf()
        plt.plot(time,function)
        plt.show()

    return function, time



test_functions(function_num=3)