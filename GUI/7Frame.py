import tkinter as tk
from PIL import ImageTk, Image 
#pip install pillow 

#From: https://youtu.be/YXPyB4XeYLA
#      From 1:59:45 to 2:07:49
#SOurce code: https://github.com/flatplanet/Intro-To-TKinter-Youtube-Course


root=tk.Tk()
root.title('Frame')

#load the icon for the GUI 
root.iconbitmap('./Physics_helper_logo.ico')


#my_img=ImageTk.PhotoImage(Image.open('./Big_Bend.png'))

frame=tk.LabelFrame(root, text='This is the frame1',padx=5,pady=5)
frame.pack(padx=10,pady=10)

#We put the label in the frame
#label=tk.Label(image=my_img)
label=tk.Label(frame,text='label1')
label.pack()

frame2=tk.LabelFrame(root, text='This is the frame2',padx=100,pady=100)
frame2.pack(padx=10,pady=10)

#We put the label in the frame
label2=tk.Label(frame2, text='Label2')
label2.pack()


#creat the GUI
root.mainloop()


