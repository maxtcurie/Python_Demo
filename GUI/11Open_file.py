import tkinter as tk
from tkinter import filedialog 
#From: https://youtu.be/YXPyB4XeYLA
#      From 2:44:30 to 2:56:09
#SOurce code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course


root=tk.Tk()
root.title('New Window')

#load the icon for the GUI 
root.iconbitmap('./Physics_helper_logo.ico')

root.filename=filedialog.askopenfilename(initialdir='./',\
									title='select a file', \
									filetypes=( 
										('python files','.py'),\
										('png files','png'),\
										('all files', '.*')
										) \
									)

mylab=tk.Label(root, text=root.filename).pack()

#creat the GUI
root.mainloop()


