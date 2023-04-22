# pip install mutagen

from mutagen.mp3 import MP3
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

# Example usage:
mp3_file = generate_filepath()+'example.mp3'
duration = get_mp3_duration(mp3_file)
print(f"The duration of '{mp3_file}' is {duration:.2f} seconds.")
