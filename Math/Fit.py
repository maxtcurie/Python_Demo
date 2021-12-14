import numpy as np
from astropy import modeling
import matplotlib.pyplot as plt
from scipy import optimize

m = modeling.models.Gaussian1D(amplitude=10, mean=30, stddev=5)
x = np.linspace(0, 100, 2000)
data = m(x)
data = data + np.sqrt(data) * np.random.random(x.size) - 0.5
data -= data.min()

#******Start of fit any function*********
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
def function(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / stddev)**2)

popt, _ = optimize.curve_fit(function, x, data)#Fit any function 

print('********function(Gaussian)fit***********')
print(*popt)
print('********function(Gaussian)fit***********')


for i in popt:
	print(i)

plt.clf()
plt.plot(x, data)
plt.plot(x, function(x, *popt))
plt.show()

#******End of fit any function*********


#******Start of fit polynomial function*********
#https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])

z=np.polyfit(x, y, 3)	#Fit and the x,y to the 3rd order 
print('********polyfit***********')
print(z)
print('********polyfit***********')

#https://numpy.org/doc/stable/reference/generated/numpy.poly1d.html
x_fit=np.arange(0,5,0.001)
y_func=np.poly1d(z)	#generate a function for the given polynomial parameters
y_fit=y_func(x_fit)
print(y_fit)

plt.clf()
plt.plot(x,y,label='original')
plt.plot(x_fit,y_fit,label='fit')
plt.legend()
plt.show()
#******Start of fit polynomial function*********