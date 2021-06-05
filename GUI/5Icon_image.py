import tkinter as tk
from PIL import ImageTk, Image 
#pip install pillow for PIL library

#From: https://youtu.be/YXPyB4XeYLA
#      From 1:18:14 to 1:28:10
#Source code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course


root=tk.Tk()
root.title('Icon')

#load the icon for the GUI 
root.iconbitmap('./Physics_helper_logo.ico')

#Load the image
my_img1=ImageTk.PhotoImage(Image.open('./Physics_helper_logo.png'))
my_img2=ImageTk.PhotoImage(Image.open('./Big_Bend.png'))


#put the image to the label
my_Label=tk.Label(image=my_img1)
my_Label.grid(row=0,column=0)

def change_image():
	#One needs to declare the global varible in order to access my_Label
	global my_Label
	#Forget the the setup for the my_Label
	my_Label.grid_forget()
	my_Label=tk.Label(image=my_img2, padx=150, pady=100)
	my_Label.grid(row=0,column=0)


#put the button
my_Button=tk.Button(root, text='Change the image',command=change_image)
my_Button.grid(row=1,column=0)

#creat the GUI
root.mainloop()


