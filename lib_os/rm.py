import os
from os import listdir
from os.path import isfile, join
path='1test_dir'
onlyfiles = [f for f in listdir(path) if (isfile(join(path, f)) and f!='.gitignore')]
print(onlyfiles)
for i in onlyfiles:
    os.remove(join(path, i))