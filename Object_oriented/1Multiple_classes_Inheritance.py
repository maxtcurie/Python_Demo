

class base_class():
	def __init__(self, var1, var2, var3):
		self.var1=var1
		self.var2=var2
		self.var3=var3

class sub_class1(base_class):
	def __init__(self, var1, var2, var3, var41):
		super().__init__(var1, var2, var3)
		self.var41=var41

class sub_class2(base_class):
	def __init__(self, var1, var2, var3, var42):
		super().__init__(var1, var2, var3)
		self.var42=var42


var1, var2, var3, var41=1,2,3,41
var42 = 42

obj1=sub_class1(var1, var2, var3, var41)
obj2=sub_class2(var1, var2, var3, var42)

print(obj1.var41)
print(obj2.var42)


class A:
	def __init__(self):
		super().__init__()
		self.var1=1 
		self.var2='class A' 

class B:
	def __init__(self):
		super().__init__()
		self.var1=1 
		self.var2='class B' 

class C(A,B):
	def __init__(self):
		super().__init__()
obj3=C()
print(obj3.var2)



#this subclass is read from left to right
class C(B,A):
	def __init__(self):
		super().__init__()
obj3=C()
print(obj3.var2)

#print out the method resolution ordering 
print(C.__mro__)

#(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

