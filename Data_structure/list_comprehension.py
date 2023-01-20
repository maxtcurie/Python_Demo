import numpy as np

a=[i*10 for i in range(10)]
print(a)

a=[i*10 for i in range(10)\
		if i%2==0]
print(a)


a=[i*j  for i in range(10)\
		for j in range(10)]
print(a)


a=['even' if i%2==0 else 'odd'  for i in range(10)]
print(a)

a=[0 if i%3==0 \
	else 1 if i%3==1 \
	else 2  \
	for i in range(10)]
print(a)

#from: https://www.geeksforgeeks.org/how-to-handle-a-python-exception-in-a-list-comprehension/

# helper function
def util_func(a):
    try:
        b=1./a
        return(b)
    except:
        return 10**10

a=[util_func(i)	for i in range(10)]
print(a)