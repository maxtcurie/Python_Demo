from PIL import Image
path='.'

for i in range(30):
	name=str(i+1)
	fig = Image.open(name+'.tif')

	if fig.mode in ('RGBA', 'LA'):
	    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html?highlight=eps#eps
	    print('Current figure mode "{}" cannot be directly saved to .eps and should be converted (e.g. to "RGB")'.format(fig.mode))
	    fig = fig.convert('RGB')
	
	out_fig = name+'.eps'
	fig.save(out_fig)
	fig.close()