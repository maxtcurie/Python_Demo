a=[i*10 for i in range(10)]
print(a)

a=[i*10 for i in range(10)\
		if i%2==0]
print(a)


a=[i*j  for i in range(10)\
		for j in range(10)]
print(a)