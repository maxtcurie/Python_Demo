class base_class():
	def __init__(self, var1=1, var2=2):
		self.var1=var1
		self.var2=var2

	#magic method return the custum string
	def __str__(self):
		return f'({self.var1}, {self.var2})'

	#magic method return the representation of the object
	def __repr__(self):
		return f'report: var1={self.var1} \nvar2={self.var2}'

	#magic function to check if two objects are euqal
	def __eq__(self, value):
		if not isinstance(value,base_class):
			raise ValueError('The comparision can only be made within the same class')
		else: 
			return (self.var1==value.var1 and \
					self.var2==value.var2)

	#magic function to check the inequality between two objects
	#this is greater or equal
	def __ge__(self, value):
		if not isinstance(value,base_class):
			raise ValueError('The comparision can only be made within the same class')
		else: 
			return (self.var1*self.var2>=value.var1*value.var2)

	#this is less than, which is need for sore the objects
	def __lt__(self, value):
		if not isinstance(value,base_class):
			raise ValueError('The comparision can only be made within the same class')
		else: 
			return (self.var1*self.var2 < value.var1*value.var2)

	#https://python-reference.readthedocs.io/en/latest/docs/dunderattr/getattribute.html
	#when one define the attribute, one can use this method to 
	#  manipulated the values stored in this attribute
	def __getattribute__(self, name):
		if name=='var1':
			v1=super().__getattribute__('var1')
			v2=super().__getattribute__('var2')
			return v1*100
		else:
			return super().__getattribute__(name)

	#this is will run if __getattribute__ is not defined, or the attribute does not exist
	def __getattr__(self, name):
		print(name+' is not here! ')
		return name+' is not here! '

	#magic call method that call object like a function
	def __call__(self,var1,var2):
		self.var1=var1
		self.var2=var2



a=base_class()
b=base_class()
c=base_class(2,4)
print(a)
print('******str********')
print('a=',str(a))
print('b=',str(b))
print('c=',str(c))
print('*******repr*******')
print(repr(a))

print('*******comparision*******')
print('a==b is ', a==b)
print('a==c is ', a==c)
print('c>=a is ', c>=a)
print('a>=c is ', a>=c)
print('a>=b is ', a>=b)

print('*******before sorting*******')
obj_list=[a,c,b]

for i in obj_list:
	print(str(i))



print('*******after sorting*******')
obj_list.sort()

for i in obj_list:
	print(str(i))


print('**************')
a=base_class()
a.var1=10
print(a)


print('**************')
#Testing the call method
a(1,2)
print(a)


print('**************')
print(a==1)