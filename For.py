for i in range(10):
	print(i)

print('*********')
i_list=['a','b','c','d','e','f']
for i in i_list:
	print(i)

print('*********')

for count, value in enumerate(i_list):
    print(count, value)

print('*********')
i_list=['a','b','c','d','e','f']
j_list=['1','2','3','4','5','6']

for (i,j) in zip(i_list,j_list):
    print(i,j)

print('*********')
for i in range(100):
	if i==10:
		continue 	#to skip the the rest of the content for this step
	elif i==19:
		break		#break out of the for loop
	print(i)

