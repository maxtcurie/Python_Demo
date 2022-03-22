import numpy as np

a = np.array([[1,4], [3,1]])
print(a)
#sorting all the 
b=np.sort(a,axis=-1)
print(b)
a.sort(axis=-1)
print(a)

a_list=[]
x_list=np.arange(0.8,1.21,0.1)

for x1 in x_list:
	for x2 in x_list:
		a_list.append([x1,x2,x1*x2])
a_list=np.array(a_list)
print('a_list')
print(a_list)

#https://www.kite.com/python/answers/how-to-sort-the-rows-of-a-numpy-array-by-a-column-in-python

order_index=np.argsort(a_list[:, 2])

a_list_sorted = a_list[order_index][:,2]

print('a_list_sorted')
print(a_list_sorted)

