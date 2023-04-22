# pip install moviepy
# pip install numpy
# pip install imageio
# pip install wand

import moviepy.editor as mp
from moviepy.video.tools.credits import credits1
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

# read the text file and split it into lines
with open(generate_filepath()+'example.txt', 'r') as file:
    lines = file.readlines()

# create a clip with the lines scrolling up
txt_clip = mp.TextClip('\n'.join(lines), fontsize=70, color='white', bg_color='black', method='caption', align='center')
scrolling_clip = txt_clip.set_pos('center').set_duration(len(lines) * 2).crossfadein(1).crossfadeout(1).resize(height=720)

# add credits to the end of the video
credits = credits1("Made with Python and MoviePy", 3, 1)
credits_clip = credits.set_duration(10).fadeout(2).resize(height=720)

# concatenate the clips
final_clip = mp.concatenate_videoclips([scrolling_clip, credits_clip])

# save the video file
final_clip.write_videofile(generate_filepath()+'example.mp4', fps=24)
