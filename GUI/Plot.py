import tkinter as tk

#https://www.geeksforgeeks.org/how-to-embed-matplotlib-charts-in-tkinter-gui/

root=tk.Tk()
root.title('New Window')

#load the icon for the GUI 
root.iconbitmap('./Physics_helper_logo.ico')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

# plot function is created for
# plotting the graph in
# tkinter window
def plot():

	# the figure that will contain the plot
	fig = Figure(figsize = (5, 5),
				dpi = 100)

	# list of squares
	y = [i**2 for i in range(101)]

	# adding the subplot
	plot1 = fig.add_subplot(111)

	# plotting the graph
	plot1.plot(y)

	# creating the Tkinter canvas
	# containing the Matplotlib figure
	canvas = FigureCanvasTkAgg(fig,
							master = root)
	canvas.draw()

	# placing the canvas on the Tkinter window
	canvas.get_tk_widget().pack()

	# creating the Matplotlib toolbar
	toolbar = NavigationToolbar2Tk(canvas,
								root)
	toolbar.update()

	# placing the toolbar on the Tkinter window
	canvas.get_tk_widget().pack()

# dimensions of the main window
root.geometry("500x500")

# button that displays the plot
plot_button = tk.Button(master = root,
					command = plot,
					height = 2,
					width = 10,
					text = "Plot")

# place the button
# in main window
plot_button.pack()


#creat the GUI
root.mainloop()


