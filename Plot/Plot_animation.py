import numpy as np
import matplotlib.pyplot as plt
import imageio

#https://medium.com/swlh/python-animated-images-6a85b9b68f86
#pip install imageio
#pip install imageio-ffmpeg
#pip install pygifsicle



image_path = './img_list/'

x=np.arange(0,1,0.001)
for i in range(10):
	plt.clf()
	plt.plot(x,x*float(i),label='y='+str(i)+'*x')
	plt.ylim(0,10)
	plt.legend()
	plt.savefig(image_path+str(i)+'.png')

image_list = []
for i in range(10):
    image_list.append(imageio.imread(image_path+str(i)+'.png'))

#duration=0.25
#loop=0 infinite loop, loop=1 just play once
imageio.mimwrite(image_path+'animated_from_images.gif', image_list, loop=0, format='gif', duration=0.25)


