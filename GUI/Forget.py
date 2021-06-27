import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 2:56:09 to 3:08:25
#Source code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course



def update():
	global Label1
	global Label2
	Label1.grid_forget()
	Label2.grid_forget()
	Label1=tk.Label(root,text=Slider1.get())
	Label1.grid(row=1,column=0)
	Label2=tk.Label(root,text=Slider2.get())
	Label2.grid(row=3,column=0)



