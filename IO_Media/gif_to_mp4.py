from moviepy.editor import *

# Load your GIF file
gif_path = 'input.gif'  # Change this to the path of your GIF file
output_path = 'output.mp4'  # Desired path for the output MP4 file

# Load the GIF using MoviePy
clip = VideoFileClip(gif_path)

# Write the clip as an MP4 file
clip.write_videofile(output_path, codec='libx264', fps=24)
