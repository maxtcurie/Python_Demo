#the library need for abstractmethod
from abc import ABC, abstractmethod

#this class will output json file
class JSONify(ABC):
	@abstractmethod
	def toJSON(self):
		pass


class base_class(ABC):
	def __init__(self, var1):
		super().__init__()
		self.var1=var1
	
	'''
	this method will be overwriteen. 
		And every subclass has to 
		overwrite this method
	'''
	@abstractmethod
	def abstract_method(self):
		self.var1=self.var1*200.

class sub_class1(base_class, JSONify):
	def __init__(self, var1):
		super().__init__(var1)

	def abstract_method(self):
		print('var1='+str(self.var1))
		print('var1**2='+str(self.var1**2.))
		return self.var1**2.

	def toJSON(self):
		return f'{{\"var1**2=\":{str(self.var1**2.)} }}'


class sub_class2(base_class, JSONify):
	def __init__(self, var1):
		super().__init__(var1)

	def abstract_method(self):
		print('var1='+str(self.var1))
		print('var1**0.5='+str(self.var1**0.5))
		return self.var1**0.5

	def toJSON(self):
		return f'{{\"var1**0.5=\":{str(self.var1**0.5)} }}'

obj1=sub_class1(10.)
obj2=sub_class2(20.)

obj1.abstract_method()
print('\n')
obj2.abstract_method()

print('*********\n')
print(obj1.toJSON())
print('\n')
print(obj2.toJSON())