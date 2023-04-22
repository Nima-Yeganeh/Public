# python.exe -m pip install --upgrade pip
# pip install gtts
# pip3 install gtts
# pip install --upgrade gtts

# pip install Pillow

# pip install moviepy
# pip install ffmpeg-python
# pip install mutagen

from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *
from mutagen.mp3 import MP3
from PIL import Image
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

# open the file and read its content
with open(generate_filepath()+'example.txt', 'r') as file:
    text = file.read().replace('\n', '\n')
print(text)

# create a gTTS object and specify the language
tts = gTTS(text, lang='en', slow=False)

# save the audio file
tts.save(generate_filepath()+'example.mp3')

# Set up the image
bg_color = (255, 255, 255)
font_color = (0, 0, 0)
font_size = 16
font = ImageFont.truetype('arial.ttf', font_size)
text_margin = 20
max_width = 1920

# Read the text file
with open(generate_filepath()+'example.txt', 'r') as f:
    text = f.read()

# Split the text into words and create a list of lines
words = text.split()
lines = []
current_line = ""
for word in words:
    if font.getsize(current_line + ' ' + word)[0] <= max_width - 2 * text_margin:
        current_line += ' ' + word if len(current_line) > 0 else word
    else:
        lines.append(current_line.strip())
        current_line = word
lines.append(current_line.strip())

# Calculate the total width and height of the image
total_width = max_width
total_height = sum(font.getsize(line)[1] for line in lines) + len(lines) * 5 + 2 * text_margin

# Create the image and draw the text
image = Image.new('RGB', (total_width, total_height), bg_color)
draw = ImageDraw.Draw(image)
y = text_margin
for line in lines:
    x = text_margin
    draw.text((x, y), line, font=font, fill=font_color)
    y += font.getsize(line)[1] + 5

# Save the image
image.save(generate_filepath()+'example.png')

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
