#tutorial on cython: https://youtu.be/mXuEoqK4bEc
def for_loop(n):
    sum0=0
    for i in range(n):
        for j in range(n):
            sum0=i**2
    return sum0


cpdef int for_loop_def_type(int n):
    cdef int sum0=0
    cdef int i
    cdef int j
    for i in range(n):
        for j in range(n):
            sum0=i**2
    return sum0