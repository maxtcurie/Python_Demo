#From: https://www.geeksforgeeks.org/moviepy-concatenating-multiple-video-files/

# Import everything needed to edit video clips
from moviepy.editor import * #pip install moviepy
import numpy as np

path='./'

x=np.arange(1,14)
x=np.arange(1,2)
x_str=x.astype("str")
x_str=[('0' + i)[-2:] for i in x_str]
filenames=[path + 'GH' + i + '0131.MP4' for i in x_str]

clip_list=[]
for filename in filenames:
	# loading video dsa gfg intro video
	clip = VideoFileClip(filename)
	clip_list.append(clip)

 
# concatenating both the clips
final = concatenate_videoclips(clip_list)
#writing the video into a file / saving the combined video
final.write_videofile(path+"merged.MP4")
 
# showing final clip
#final.ipython_display(width = 480)
