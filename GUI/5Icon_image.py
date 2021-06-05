import tkinter as tk
from PIL import ImageTk, Image 
#pip install pillow 

#From: https://youtu.be/YXPyB4XeYLA
#      From 1:18:14 to 1:28:10
#SOurce code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course


root=tk.Tk()
root.title('Icon')

#load the icon for the GUI 
root.iconbitmap('./Physics_helper_logo.ico')

#Load the image
my_img=ImageTk.PhotoImage(Image.open('./Physics_helper_logo.png'))

#put the image to the label
my_Label=tk.Label(image=my_img)
my_Label.pack()

#creat the GUI
root.mainloop()


