
import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 0:00 to 10:21
root=tk.Tk()

#create the label
myLabel=tk.Label(root,text='Hello World!!!',\
	font= "Helvetica 40 bold italic",\
	fg='white',bg='green')

#pack the label on the screen
myLabel.pack()

#creat the GUI
root.mainloop()

