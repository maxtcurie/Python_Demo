import numpy as np

n=2

a=np.random.rand(n,n)
print('a')
print(a)
print('******************\n\n')

print('******************')
print('Multiply each matrix elements')
print('a*a')
print(a*a)
print('******************\n\n')

print('******************')
print('np.multiply(a,a)')
print(np.multiply(a,a))
print('******************\n\n')

print('******************')
print('matrix multiplication')
print('np.matmul(a,a)')
print(np.matmul(a,a))
print('******************\n\n')

print('******************')
print('matrix multiplication')
print('np.linalg.inv(a)')
print(np.linalg.inv(a))
print('******************\n\n')

