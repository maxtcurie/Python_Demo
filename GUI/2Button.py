
import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 20:10 to 29:57
root=tk.Tk()

def myClick():
	i=0
	myLable=tk.Label(root, text='You have click the button'+str(i)+'times')
	myLable=tk.Label(root, text='You have click the button')
	myLable.grid(row=4,column=0)



#create the label
myLabel1=tk.Label(root,text='Label1')
myLabel2=tk.Label(root,text='Label1')
#creat button
myButton1=tk.Button(root, text='Click me',\
					command=myClick,\
					#to execute the command after the click of this button
					#no () 
					padx=50, pady=10,\
					#size of button of x(width), y(height)
					fg='blue',\
					#color of the label in the button 
					bg='red')
					#color of the button 

myButton2=tk.Button(root, text='Click me(disabled)',\
					 state=tk.DISABLED)#state: tk.DISABLED, or tk.NORMAL

#pack the label on the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

#pack the button on the screen
myButton1.grid(row=2,column=0)
myButton2.grid(row=3,column=0)


#creat the GUI
root.mainloop()


