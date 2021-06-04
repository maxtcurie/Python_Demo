
import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 39:07 to 1:18:14
root=tk.Tk()
root.title('Simple calculator')

#Creat input box 
Input_box=tk.Entry(root, width=35,borderwidth=5)
Input_box.grid(row=0,column=0,columnspan=3, padx=10,pady=10)

def button_add():
	i=float(Input_box.get())
	myLable_TEMP=tk.Label(root, text=str(i)+'^2='+str(i**2.))
	myLable_TEMP.pack()

button_number_list=[]

for i in range(10):
	button_TEMP=tk.Button(root, text=str(i), padx=40, pady=20, command=button_add)
#crea the label
myLable=tk.Label(root, text='Do the square by clicking th button')
myLable.pack()

#creat button
myButton1=tk.Button(root, text='Click me',command=myClick)
myButton1.pack()


#creat the GUI
root.mainloop()


