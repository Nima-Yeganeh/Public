# pip install Pillow

from PIL import Image, ImageDraw, ImageFont
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

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
