import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 2:56:09 to 3:08:25
#Source code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course

#https://www.tutorialspoint.com/python/tk_checkbutton.htm

root=tk.Tk()
root.title('Dropdown Menus')
root.iconbitmap('./Physics_helper_logo.ico')

clicked=tk.StringVar()
clicked.set('Choose the Options')

Options=['Option1','Option2','Option3']
#add the dropdown menu
drop=tk.OptionMenu(root, clicked, *Options)
drop.pack()

def update():
	print(clicked.get())

tk.Button(root,text='Click me',command=update).pack()


#creat the GUI
root.mainloop()


