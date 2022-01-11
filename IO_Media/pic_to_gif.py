import imageio
import numpy as np
#from: https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python

path='./Output/'

x=np.arange(10)
x_str=x.astype("str")
filenames=[path +i + '.png' for i in x_str]
filenames_sin=[path + i + '_sin.png' for i in x_str]

with imageio.get_writer(path+'movie.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

with imageio.get_writer(path+'movie_sin.gif', mode='I') as writer:
    for filename in filenames_sin:
        image = imageio.imread(filename)
        writer.append_data(image)