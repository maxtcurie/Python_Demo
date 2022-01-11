import numpy as np

path='./Output/'

x=np.arange(10)
x_str=x.astype("str")
filenames=[path +i + '.png' for i in x_str]
filenames_sin=[path + i + '_sin.png' for i in x_str]
