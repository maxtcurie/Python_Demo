import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 2:56:09 to 3:08:25
#Source code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course


root=tk.Tk()
root.title('New Window')
root.geometry('400x400')

#load the icon for the GUI 
root.iconbitmap('./Physics_helper_logo.ico')

#create a slider
Slider1=tk.Scale(root, from_=0, to=100)
Slider1.grid(row=0,column=0)

Slider2=tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
Slider2.grid(row=2,column=0)

Label1=tk.Label(root,text=Slider1.get())
Label1.grid(row=1,column=0)
Label2=tk.Label(root,text=Slider2.get())
Label2.grid(row=3,column=0)

def update():
	global Label1
	global Label2
	Label1.grid_forget()
	Label2.grid_forget()
	Label1=tk.Label(root,text=Slider1.get())
	Label1.grid(row=1,column=0)
	Label2=tk.Label(root,text=Slider2.get())
	Label2.grid(row=3,column=0)

tk.Button(root, text='Update the number',command=update).grid(row=4,column=0)

#creat the GUI
root.mainloop()


