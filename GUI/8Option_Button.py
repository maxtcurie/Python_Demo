import tkinter as tk
from PIL import ImageTk, Image 
#pip install pillow 

#From: https://youtu.be/YXPyB4XeYLA
#      From 2:07:49 to 2:24:36
#SOurce code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course


root=tk.Tk()
root.title('Option Button')

#load the icon for the GUI 
root.iconbitmap('./Physics_helper_logo.ico')

opt_var1= tk.IntVar() #Integar Varible, Other options: StringVar()
opt_var2= tk.IntVar()

#Set the default option as option1
opt_var1.set(1)

frame1=tk.LabelFrame(root, text='question1',padx=50,pady=40)
frame1.pack()
tk.Label(frame1,text='Question1 has 2 options').grid(row=0,column=0)

frame2=tk.LabelFrame(root, text='question2',padx=50,pady=60)
frame2.pack()
tk.Label(frame2, text='Question2 has 3 options').pack()

Label1=tk.Label(frame1, text='You chose option1')
Label1.grid(row=3,column=0)

def click_button(value):
	global Label1
	Label1.grid_forget()
	Label1=tk.Label(frame1, text='You chose option'+str(value))
	Label1.grid(row=3,column=0)

#import an option button
option_button11=tk.Radiobutton(frame1, text='Option1',\
							variable=opt_var1, value=1,\
							command=lambda: click_button(opt_var1.get()))
option_button11.grid(row=1,column=0)

option_button12=tk.Radiobutton(frame1, text='Option2',\
							variable=opt_var1, value=2,\
							command=lambda: click_button(opt_var1.get()))
option_button12.grid(row=2,column=0)



#import an option button
option_button21=tk.Radiobutton(frame2, text='Option1',variable=opt_var2, value=1)
option_button21.pack()

option_button22=tk.Radiobutton(frame2, text='Option2',variable=opt_var2, value=2)
option_button22.pack()

option_button23=tk.Radiobutton(frame2, text='Option3',variable=opt_var2, value=3)
option_button23.pack()


#creat the GUI
root.mainloop()


