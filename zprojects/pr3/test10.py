# pip install moviepy
# pip install ffmpeg-python

from moviepy.editor import *
from mutagen.mp3 import MP3
from PIL import Image

import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

def get_mp3_duration(filename):
    audio = MP3(filename)
    duration = audio.info.length
    return duration

def get_png_resolution_width(filename):
    with Image.open(filename) as img:
        width, height = img.size
        return f"{width}", f"{height}"

# Set up the video
mp3_file = generate_filepath()+'example.mp3'
duration = get_mp3_duration(mp3_file)
# duration = 10  # in seconds
fps = 1
# width, height = 1920, 110
png_file = generate_filepath()+'example.png'
xwidth, xheight = get_png_resolution_width(png_file)
width = str(xwidth)
height = int(xheight)
if height % 2 != 0:
    height += 1
print(width,height)

# Load the PNG file as a clip
image_clip = ImageClip(generate_filepath()+'example.png').set_duration(duration).resize((width, height))

# Load the MP3 file as an audio clip
audio_clip = AudioFileClip(generate_filepath()+'example.mp3').set_duration(duration)

# Combine the image and audio clips
video_clip = image_clip.set_audio(audio_clip)

# Write the combined clip to an MP4 file
video_clip.write_videofile(generate_filepath()+'example.mp4', fps=fps)
