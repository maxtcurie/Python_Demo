import numpy as np

#tutorial on cython: https://youtu.be/mXuEoqK4bEc
def matrix_inversion(n):
    a=np.random.rand(n,n)
    return np.linalg.inv(a)


#define array in cython: https://cython.readthedocs.io/en/latest/src/tutorial/array.html
from cpython cimport array
import array
cdef array.array a = array.array('i', [1, 2, 3])
cdef int[:] ca = a

cpdef float matrix_inversion_def_type(int n):
    a=np.random.rand(n,n)
    return np.linalg.inv(a)    
