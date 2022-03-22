from os import listdir
from os.path import isfile, join
mypath='1test_dir'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)