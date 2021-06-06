import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 2:56:09 to 3:08:25
#Source code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course


root=tk.Tk()
root.title('Overview')
root.iconbitmap('./Physics_helper_logo.ico')

#*******************Label*****************
#Label
tk.Label(root,text='Label').pack()
#*******************Label*****************


#******************Button*******************
def update():
	i=1+1
#Button
tk.Button(root,text='Click me',command=update).pack()
#******************Button*******************


#*******************label**********************
#creat the label
Input_box=tk.Entry(root, width=50, bg='green', fg='white')
Input_box.insert(0,'Enter the number')
Input_box.pack()
#*******************label**********************

#*********option button******************
def click_button(value):
	tk.Label(root, text='You chose option'+str(value)).pack()

#import an option button
opt_var1=tk.IntVar()
option_button11=tk.Radiobutton(root, text='Option1',\
							variable=opt_var1, value=1,\
							command=lambda: click_button(opt_var1.get()))
option_button11.pack()

option_button12=tk.Radiobutton(root, text='Option2',\
							variable=opt_var1, value=2,\
							command=lambda: click_button(opt_var1.get()))
option_button12.pack()
#*********option button******************


#*********Message box*************************
from tkinter import messagebox
def pop_up():
	#A pop up message box: showinfo, showerror, askquestion, askokcancel, askyesno
	#tk.messagebox.showinfo('This is popup', 'Hello!')
	#tk.messagebox.showerror('This is popup', 'Warning!')
	response = tk.messagebox.askyesno('This is popup', 'Yes or No')
	tk.Label(root,text=response).pack()
	# 				Title of the pop-up, Info in the popup

tk.Button(root, text='Click for pop-up',command=pop_up).pack()
#*********Message box*************************

#****************file*************************
from tkinter import filedialog 
root.filename=filedialog.askopenfilename(initialdir='./',\
									title='select a file', \
									filetypes=( 
										('python files','.py'),\
										('png files','png'),\
										('all files', '.*')
										) \
									)
mylab=tk.Label(root, text=root.filename).pack()
#****************file*************************


#**************slider*********************
#create a slider
Slider1=tk.Scale(root, from_=0, to=100).pack()
Slider2=tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL).pack()
#**************slider*********************

#****************checkbox***************
var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()
#Load a checkbox
c1=tk.Checkbutton(root, text='option1', variable=var1,\
					onvalue=1,offvalue=0)
c2=tk.Checkbutton(root, text='option2', variable=var2,\
					onvalue=1,offvalue=0)
c3=tk.Checkbutton(root, text='option3', variable=var3,\
					onvalue=1,offvalue=0)
#****************checkbox***************


#***************dropdown menu****************
clicked=tk.StringVar()
clicked.set('Choose the Options')

Options=['Option1','Option2','Option3']

#add the dropdown menu
drop=tk.OptionMenu(root, clicked, *Options)
drop.pack()
#***************dropdown menu****************



#creat the GUI
root.mainloop()


