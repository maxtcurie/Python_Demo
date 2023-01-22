import zipfile
try:
	# Unzip the archive
	local_zip = './Input/1cats_and_dogs_filtered.zip'
	zip_ref = zipfile.ZipFile(local_zip, 'r')
	zip_ref.extractall('1cats_and_dogs_filtered')
	zip_ref.close()
except:
	import wget #pip install wget
	print('Beginning file download with wget module')

	url = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
	wget.download(url, './Input/1cats_and_dogs_filtered.zip')
