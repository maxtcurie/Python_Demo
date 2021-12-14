import numpy as np
from astropy import modeling
import matplotlib.pyplot as plt
from scipy import optimize

m = modeling.models.Gaussian1D(amplitude=10, mean=30, stddev=5)
x = np.linspace(0, 100, 2000)
data = m(x)
data = data + np.sqrt(data) * np.random.random(x.size) - 0.5
data -= data.min()

'''
plt.plot(x, data)

fitter = modeling.fitting.LevMarLSQFitter()
model = modeling.models.Gaussian1D()   # depending on the data you need to give some initial values
fitted_model = fitter(model, x, data)

plt.plot(x, data)
plt.plot(x, fitted_model(x))
'''




def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / stddev)**2)

popt, _ = optimize.curve_fit(gaussian, x, data)

print(*popt)

for i in popt:
	print(i)


plt.clf()
plt.plot(x, data)
plt.plot(x, gaussian(x, *popt))
plt.show()