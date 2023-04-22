# pip install Pillow

from PIL import Image
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

def get_png_resolution(filename):
    with Image.open(filename) as img:
        width, height = img.size
        resolution = f"{width}x{height}"
        return resolution

def get_png_resolution_width(filename):
    with Image.open(filename) as img:
        width, height = img.size
        return f"{width}", f"{height}"

# Example usage:
png_file = generate_filepath()+'example.png'
resolution = get_png_resolution(png_file)
print(f"The resolution of '{png_file}' is {resolution}.")
xwidth, xheight = get_png_resolution_width(png_file)
print(xwidth)
print(xheight)
