import matplotlib.pyplot as plt
import numpy as np

#Video about Pitfalls in FFT: https://youtu.be/jZVekQ2ZDXQ

a=-2-1.j
print('a='+str(a))

print('a^2='+str(a**2.))
print('(a^2)^(1/2)='+str((a**2.)**0.5))


fs = 10e4
N = 1000
time = np.arange(N) / fs
omega=2.*np.pi*200
function=np.exp(-1.j * omega * time -3.j)+0.5*np.exp(+1.j * 2*omega * time-1.j)

plt.clf()
plt.plot(time,np.real(function),label='real')
plt.plot(time,np.imag(function),label='imag')
plt.legend()
plt.grid()
plt.title('function')
plt.show()


function1=((function)**2.)**0.5

plt.clf()
plt.plot(time,np.real(function1),label='real')
plt.plot(time,np.imag(function1),label='imag')
plt.legend()
plt.grid()
plt.title('((function)**2.)**0.5')
plt.show()

