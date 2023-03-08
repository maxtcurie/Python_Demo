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

a=np.random.rand(2*n,n)
b=np.random.rand(n)
print('******************')
print('np.divide(a,b)')
print(np.divide(a,(b**2.)))
print('******************\n\n')
print(np.divide(a,(b**2.).T))
print('******************\n\n')
