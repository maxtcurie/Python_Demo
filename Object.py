import numpy as np
import matplotlib.pyplot as plt

#From https://youtu.be/MikphENIrOo


class Dot_object:
	#function to initiate
	def __init__(self,x,y):
		self.x=x
		self.y=y
		print('initiated')

	def x_times_y(self):
		return self.x*self.y

	def a_2(self,a1,a2):
		return a1*a2

	def x_times_y_times_a_1(self,a):
		return self.x*self.y*a

	def x_times_y_times_a_2(self,a):
		return self.x_times_y()*self.a_2(a,a)


c=Dot_object(5,2)
print(c)
print(c.x)
print(c.y)

print(c.x_times_y())
print(c.x_times_y_times_a_1(2))
print(c.x_times_y_times_a_2(2))

