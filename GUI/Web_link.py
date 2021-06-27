import tkinter as tk

#https://stackoverflow.com/questions/23482748/how-to-create-a-hyperlink-with-a-label-in-tkinter

root=tk.Tk()
root.title('New Window')

#load the icon for the GUI 
root.iconbitmap('./Physics_helper_logo.ico')

import webbrowser
def callback(url):
    webbrowser.open_new(url)
link1 = tk.Label(root, text="Google Hyperlink", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))


#creat the GUI
root.mainloop()


