import os 
path='tmp'
try: 
    os.mkdir(path)
except:
    pass

import gdown #pip install gdown
print('Beginning file download with gdown module')

id_='15UqmiIm0xwh9mt0IYq2z3jHaauxQSTQT'
url='https://drive.google.com/u/1/uc?id='+id_
gdown.download(url,'./tmp/irish-lyrics-eof.txt')


import wget #pip install wget
print('Beginning file download with wget module')

url = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
wget.download(url, './tmp/cats_and_dogs_filtered.zip')


