import numpy as np
import matplotlib.pyplot as plt

name = 'sin(x)cos(y)'

x = np.arange(0, 6, 0.01)
y = np.arange(0, 7, 0.01)
x, y = np.meshgrid(x, y)
z = np.sin(x) * np.cos(y)

print(np.shape(x))
print(np.shape(y))
print(np.shape(z))

plt.clf()
plt.ylabel(r'$k_y \rho_s$', fontsize=10)
plt.xlabel(r'$f(kHz)$', fontsize=10)
plt.contourf(y, x, z)
plt.colorbar()
plt.title(str(name) + ' contour plot', fontsize=10)
plt.show()

plt.clf()
plt.ylabel(r'$k_y \rho_s$', fontsize=10)
plt.xlabel(r'$f(kHz)$', fontsize=10)
plt.contourf(x)
plt.colorbar()
plt.title(str(name) + ' contour plot', fontsize=10)
plt.show()

plt.clf()
plt.ylabel(r'$k_y \rho_s$', fontsize=10)
plt.xlabel(r'$f(kHz)$', fontsize=10)
plt.contourf(y)
plt.colorbar()
plt.title(str(name) + ' contour plot', fontsize=10)
plt.show()
