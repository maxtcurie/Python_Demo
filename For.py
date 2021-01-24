for i in range(10):
	print(i)

print('*********')
i_list=['a','b','c','d','e','f']
for i in i_list:
	print(i)

print('*********')
for i in range(100):
	if i==10:
		continue 	#to skip the the rest of the content for this step
	elif i==19:
		break		#break out of the for loop
	print(i)