
class Dot_object:

	#define the properties at the class level that is shared by all instances
	Dot_Types=('Type 0','Type 1','Type 2')

	#create an exmpty pravite varible
	__dotlist=None

	#create a class method
	@classmethod
	def GetType(cls):
		print('class type is '+str(cls.Dot_Types))
		return cls.Dot_Types

	@staticmethod
	def getdotlist():
		if Dot_object.__dotlist == None:
			Dot_object.__dotlist = []
		return Dot_object.__dotlist

	#function to initiate
	def __init__(self,x,y,Dot_Types_input):
		#self is the the class itself

		#attributes: this are the properties of the objects
		self.x=x
		self.y=y
		if Dot_Types_input not in Dot_object.Dot_Types:
			raise ValueError(f'{Dot_Types_input} is not a valid dot type')
		else: 
			self.Dot_Types	= Dot_Types_input

		print('initiated')

	# instance method: function of within the class
	def x_times_y(self):
		return self.x*self.y

	#One can create method with additional variable outside of the object's attribute
	def x_times_y_times_a(self,a):
		return self.x*self.y*a

	def Set_pravite_variable(self):
		#for the variable that is internal to the class, cannot be accessed outside of the class. 
		self._PraviteVar=10

	def Check_Attribute(self):
		if hasattr(self,'_PraviteVar'):
			print('has attribute _PraviteVar')
		else: 
			print('does not have attribute _PraviteVar')



#create the instances of the class
c=Dot_object(5,2,'Type 0')

#Check the type of the class
print(type(c))

#Check if c is the instance Dot_object
print(isinstance(c, Dot_object))

#print out the object
print(c)

#print the property 'x' of the object
print(c.x)
print(c.y)

print(c.x_times_y())
print(c.x_times_y_times_a(2))


#print out the class attribute
c.GetType()

#check if c has attribute '_PraviteVar'
c.Check_Attribute()

#set attribute '_PraviteVar' into c 
c.Set_pravite_variable()
c.Check_Attribute()


#creat the dotlist if it is empty 
theDots=Dot_object.getdotlist()
print(theDots)

theDots.append(c)
print(theDots)


#d=Dot_object(5,2,'Type 4')


#Appendix: 
'''
For more detail, please check the README

********Jargon list***********
********My loose definitions********
Class: Kind of like a library with structure and functions
Instances: Kind of like a variable 
Attributes: the properties of the objects
Decorator: include classmethod, staticmethod, normal method
				{
				classmethod: 	the 1st argument will be cls;

				staticmethod: 	1st argument is varible, 
								therefore cannot access or edit the 
								info about class;

				abstractmethod: if a same method is define in the multiple
								subclasses, one may need to use abstract method
								to aviod the error.
								ABC -- abstract base class
								https://docs.python.org/3/library/abc.html

				normal method: 	the 1st argument is self
				 }

			resource: https://www.geeksforgeeks.org/class-method-vs-static-method-python/
instance method: Kind of like function of within the class
'''