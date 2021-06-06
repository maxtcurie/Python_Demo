import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 2:56:09 to 3:08:25
#Source code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course

#https://www.tutorialspoint.com/python/tk_checkbutton.htm

root=tk.Tk()
root.title('CheckBox')
root.iconbitmap('./Physics_helper_logo.ico')

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

c1.grid(row=0,column=0)
c2.grid(row=1,column=0)
c3.grid(row=2,column=0)

label_text='The options are chosen are:'
Label1=tk.Label(root,text=label_text)
Label1.grid(row=3,column=0)

def show():
	global Label1
	var_list=[var1.get(),var2.get(),var3.get()]
	print(var_list)
	label_text='The options are chosen are:'
	for i in range(len(var_list)):
		j=i+1
		if var_list[i]==1:
			label_text=label_text+' option'+str(j)
	Label1.grid_forget()
	Label1=tk.Label(root,text=label_text)
	Label1.grid(row=3,column=0)

def clear_selection():
	global c1
	global c2
	global c3
	c1.deselect()
	c2.deselect()
	c3.deselect()
	show()


tk.Button(root, text='update the selection',command=show).grid(row=4,column=0)
tk.Button(root, text='clear the selection',command=clear_selection).grid(row=5,column=0)

#creat the GUI
root.mainloop()


