import os

#https://www.geeksforgeeks.org/python-os-fchdir-method/

dir_name='./'

os.chdir(dir_name)
print("Current working directory:", os.getcwd()) 

os.chdir(dir_name+'Test_path')
print("Current working directory:", os.getcwd()) 