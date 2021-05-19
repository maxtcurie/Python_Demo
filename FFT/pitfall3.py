import matplotlib.pyplot as plt
import numpy as np


fs = 10e4
N = 1000
time = np.arange(N) / fs


omega=2.*np.pi*200
function=np.exp(-1.j * omega * time -3.j)+0.5*np.exp(+1.j * 2*omega * time-1.j)

norm=1./float(len(time))  #normalizing factor

dt=time[:-1]-time[1:]
timestep=np.mean(dt)

amplitude_complex = np.fft.fft(function)
#print(str(time.shape[-1]))
#output_x = np.fft.fftfreq(t.shape[-1])
frequency = np.fft.fftfreq(time.shape[-1], d=timestep)
amplitude_frequency=abs(norm*amplitude_complex)
#amplitude_frequency=norm*amplitude_complex.real
phase_frequency=np.angle(amplitude_complex)

plt.clf()
plt.ylabel(r'$amplitude$',fontsize=10)
plt.xlabel(r'$frequency$',fontsize=10)
#plt.axvline(frequency,color='red', label="correct frequency")
#plt.axvline(2.*frequency,color='red', label="correct frequency")
plt.plot(frequency,amplitude_frequency,label="frequency")
plt.legend()
plt.title('FFT',fontsize=20)
plt.show()


uni_frequency = np.linspace(min(frequency),max(frequency),int(len(frequency)*1.5)) #uniform time
uni_amplitude_frequency = np.interp(uni_frequency,frequency,amplitude_frequency)


def sort_x_f(x_unsort,f_unsort): 
    arr_unsort=[x_unsort,f_unsort]
    f_x_unsort=tuple(map(tuple, np.transpose(arr_unsort)))
      
    f_x_sort=sorted(f_x_unsort, key=lambda f_x_unsort: f_x_unsort[0])
    f_x_sort=np.array(f_x_sort)
    f_x_sort=np.transpose(f_x_sort)
    x_sort=f_x_sort[0,:]
    f_sort=f_x_sort[1,:]

    return x_sort,f_sort


frequency_sorted,amplitude_frequency_sorted=sort_x_f(frequency,amplitude_frequency)

uni_frequency_sorted = np.linspace(min(frequency_sorted),max(frequency_sorted),int(len(frequency_sorted)*1.5)) #uniform time
uni_amplitude_frequency_sorted = np.interp(uni_frequency_sorted,frequency_sorted,amplitude_frequency_sorted)

plt.clf()
plt.ylabel(r'$frequency$',fontsize=10)
plt.xlabel(r'$index$',fontsize=10)
#plt.axvline(frequency,color='red', label="correct frequency")
#plt.axvline(2.*frequency,color='red', label="correct frequency")
plt.plot(frequency,label="frequency")
plt.plot(frequency_sorted,label="frequency sorted")
plt.title('frequency',fontsize=20)
plt.legend()
plt.show()

plt.clf()
plt.ylabel(r'$amplitude$',fontsize=10)
plt.xlabel(r'$frequency$',fontsize=10)
#plt.axvline(frequency,color='red', label="correct frequency")
#plt.axvline(2.*frequency,color='red', label="correct frequency")
plt.plot(uni_frequency,uni_amplitude_frequency,alpha=0.5,label='interpolate not sorted')
plt.plot(uni_frequency_sorted,uni_amplitude_frequency_sorted,alpha=0.5,label='interpolate sorted')
plt.legend()
plt.title('interpolate amplitude',fontsize=20)
plt.show()
