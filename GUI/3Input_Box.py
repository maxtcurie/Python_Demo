
import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 29:32 to 39:07
root=tk.Tk()

#Creat input box 
Input_box=tk.Entry(root, width=50, bg='green', fg='white')
Input_box.insert(0,'Enter the number')
Input_box.pack()

def myClick():
	i=float(Input_box.get())
	myLable_TEMP=tk.Label(root, text=str(i)+'^2='+str(i**2.))
	myLable_TEMP.pack()

#creat the label
myLable=tk.Label(root, text='Do the square by clicking th button')
myLable.pack()

#creat button
myButton1=tk.Button(root, text='Click me',command=myClick)
myButton1.pack()


#creat the GUI
root.mainloop()


