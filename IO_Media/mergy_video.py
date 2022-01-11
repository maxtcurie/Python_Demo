#From: https://www.geeksforgeeks.org/moviepy-concatenating-multiple-video-files/

# Import everything needed to edit video clips
from moviepy.editor import * #pip install moviepy
 
path='./Output/'
# loading video dsa gfg intro video
clip1 = VideoFileClip(path+"movie.gif")
clip2 = VideoFileClip(path+"movie_sin.gif")
# getting subclip as video is large
#clip1 = clip.subclip(0, 5)
 
# concatenating both the clips
final = concatenate_videoclips([clip1, clip2])
#writing the video into a file / saving the combined video
final.write_videofile(path+"merged.gif")
 
# showing final clip
#final.ipython_display(width = 480)
