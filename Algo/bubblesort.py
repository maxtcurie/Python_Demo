
import numpy as np 			#import numpy library and give it a short name as np

n=100

a=np.arange(n)

np.random.shuffle(a)

#print(a)
#https://youtu.be/YHm_4bVOe1s
def bubble_sort(a):
	n=len(a)
	for i in range(n):
		for j in range(n-1-i):
			if a[j]>a[j+1]:
				a[j],a[j+1]=a[j+1],a[j]

	return a 

def quick_sort(a):
	quick_sort_sub(a,0,len(a)-1)

def quick_sort_sub(a,low,high):
	n=len(a)
	n_2=int(n/2)



print(bubble_sort(a))
print(quick_sort(a))
