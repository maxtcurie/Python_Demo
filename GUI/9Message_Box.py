import tkinter as tk
from tkinter import messagebox
#From: https://youtu.be/YXPyB4XeYLA
#      From 2:07:49 to 2:24:36
#SOurce code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course


root=tk.Tk()
root.title('Message box')

#load the icon for the GUI 
root.iconbitmap('./Physics_helper_logo.ico')

def pop_up():
	#A pop up message box: showinfo, showerror, askquestion, askokcancel, askyesno
	#tk.messagebox.showinfo('Hello!','This is popup')
	#tk.messagebox.showerror('Warning!','This is popup')
	response = tk.messagebox.askyesno('Yes or No','This is popup')
	tk.Label(root,text=response).pack()
	# 				Title of the pop-up, Info in the popup

tk.Button(root, text='Click for pop-up',command=pop_up).pack()


#creat the GUI
root.mainloop()


