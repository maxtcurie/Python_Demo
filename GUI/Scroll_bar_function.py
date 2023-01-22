

import tkinter as tk

#From: https://youtu.be/YXPyB4XeYLA
#      From 0:00 to 10:21
root_=tk.Tk()

def Scrollbar_gen(root_):
	#my_canvas in main_frame in root
	main_frame=tk.Frame(root_)
	main_frame.pack(fill='both',expand=1)
	my_canvas=tk.Canvas(main_frame)
	my_canvas.pack(side='left',fill='both',expand=1)

	#add scroll_bar
	my_scrollbar = tk.Scrollbar(main_frame,orient='vertical',command=my_canvas.yview)
	my_scrollbar.pack(side='right',fill='y')

	#configure canvas
	my_canvas.configure(yscrollcommand=my_scrollbar.set)
	my_scrollbar.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))

	#create another frame is the canvas
	root=tk.Frame(my_canvas)

	#add root to a window
	my_canvas.create_window((0,0),window=root,anchor='nw')
	return root


root=Scrollbar_gen(root_)
#create the label
for i in range(20):
	myLabel=tk.Label(root,text='Hello World')
	myLabel.pack()



#creat the GUI
root_.mainloop()



