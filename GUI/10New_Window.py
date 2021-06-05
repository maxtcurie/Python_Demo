import tkinter as tk
from PIL import ImageTk, Image 
#From: https://youtu.be/YXPyB4XeYLA
#      From 2:07:49 to 2:24:36
#SOurce code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course


root=tk.Tk()
root.title('New Window')

#load the icon for the GUI 
root.iconbitmap('./Physics_helper_logo.ico')

def new_window():
	global my_img
	top=tk.Toplevel()
	top.title('Second winow')
	top.iconbitmap('./Physics_helper_logo.ico')
	my_img=ImageTk.PhotoImage(Image.open('./Big_Bend.png'))
	tk.Label(top,image=my_img, padx=150, pady=100).pack()
	tk.Button(top,text='Close',command=top.destroy).pack()
	#tk.Button(top,text='New Window',command=new_window).pack()

tk.Button(root,text='New Window',command=new_window).pack()


#creat the GUI
root.mainloop()


