import numpy as np 

#from: https://numpy.org/doc/stable/reference/generated/numpy.savez.html

file_name='./IO/array.npz'

a=np.random.rand(10)
b=a*10.

#saving the numpy array(s) to file_name
np.savez(file_name, a, b)
print('file saved')

#loading numpy array(s) from file_name
npzfile = np.load(file_name)
print(npzfile.files)

for i in range(len(npzfile.files)):
    array=npzfile[npzfile.files[i]]
    print(array)