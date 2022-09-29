
from PIL import Image

filenames=[str(i+1) for i in range(18)]
path='./media_file/'

for filename in filenames:
	img = Image.open(path+filename+'.png')
	img = img.convert('RGB')
	img.save(path+filename+'.pdf')