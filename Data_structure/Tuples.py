#https://youtu.be/NI26dqhs2Rk

import sys

#tuple
print('tuple')
tuple_=(1,2,3)
print(tuple_.__dir__())
tuple_mem_size=sys.getsizeof(tuple_)
print('memory size: '+str(tuple_mem_size))

print('\n\n*****************\n\n')
print('list')
list_=[1,2,3]
list_mem_size=sys.getsizeof(list_)
print(list_.__dir__())
print('memory size: '+str(list_mem_size))
