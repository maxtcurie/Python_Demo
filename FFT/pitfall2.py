import matplotlib.pyplot as plt
import numpy as np

#Video about Pitfalls in FFT: https://youtu.be/jZVekQ2ZDXQ

fs = 10e4
N = 1000
time0 = np.arange(N) / fs

time_mod=np.linspace(0,1,len(time0))
time_mod=time_mod**2.
time=time0*time_mod

plt.clf()
plt.plot(time,label='uneven time')
plt.plot(time0,label='even time')
plt.legend()
plt.show()


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
plt.title('FFT of uneven time space',fontsize=20)
plt.show()


dt_min=np.mean(abs(dt))
uni_time = np.linspace(min(time),max(time),int(abs((max(time)-min(time))/dt_min)*1.5)) #uniform time
uni_function = np.interp(uni_time,time,function)

norm=1./float(len(uni_time))  #normalizing factor

dt=uni_time[:-1]-uni_time[1:]
timestep=dt[0]

amplitude_complex = np.fft.fft(uni_function)
#print(str(time.shape[-1]))
#output_x = np.fft.fftfreq(t.shape[-1])
frequency = np.fft.fftfreq(uni_time.shape[-1], d=timestep)
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
plt.title('FFT after interpolation',fontsize=20)
plt.show()