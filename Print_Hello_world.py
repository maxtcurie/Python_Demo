#About input and output: https://docs.python.org/3/tutorial/inputoutput.html

name=input('the name: ')
age=int(input('the age: '))

print('Hello '+name+', you are  '+str(age)+' years old')

print(f'Your age is {age}.')
print('{1} and {0}'.format('spam', 'eggs'))
print('{0} and {1}'.format(1, 111))
print('This {food} is {adjective}.'.format(\
	food='spam', adjective='absolutely horrible'))

pi=3.14159265359
#For more on Format the output: https://www.python-course.eu/python3_formatted_output.php
print('%.3f'%pi)  #pi with 3 digits

print('%.3f, %.3f'%(pi,2.*pi))  #pi with 3 digits
