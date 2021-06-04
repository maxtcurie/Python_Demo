
import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 10:40 to 19:50
root=tk.Tk()

#create the label
myLabel1=tk.Label(root,text='Label1')
myLabel2=tk.Label(root,text='Label1')

#pack the label on the screen
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

#creat the GUI
root.mainloop()

