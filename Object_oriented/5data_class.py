from dataclasses import dataclass, field
import random

def function():
	return float(random.randrange(0,100)/100.)

@dataclass(frozen=False) #change frozen to True if one doesn't want to change the data once created
class data_class:
	var1: int  = 0								#integer that defaul value is 0
	var2: int  = 0  							#integer that defaul value is 0
	var3: float=field(default_factory=function)	#float   that defaul value is defined by a function
	var4: str  =field(default='None')			#string  that defaul value is 'None'

	#__post_init__ method is like __init__ is normal class
	def __post_init__(self):
		self.description=f'{self.var4}! var1={self.var1}, var2={self.var2}, var3={self.var3}'

obj1=data_class(1, 2, 2.5, 'hello world')
obj2=data_class(1, 2)
obj3=data_class()

#equal works just like the magic method
print('obj1==obj2 is ', obj1==obj2)


print(obj1.description)
print(obj2.description)
print(obj3.description)
