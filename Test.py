
nmax=4
n_list=[]

for n0 in range(nmax):
	for n1 in range(nmax):
		for n2 in range(nmax):
			if n0+2*n1-3*n2==0:
				n_list.append([n0,n1,n2])



print(n_list)
print(lne(n_list))