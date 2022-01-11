from PIL import Image
path='C:/Users/tx686/Downloads/APS paper/Fig'

for i in range(30):
	name=str(i+1)
	im1 = Image.open(path+'/'+name+'.png') 
	im1.save(path+'/'+name+'.tif')