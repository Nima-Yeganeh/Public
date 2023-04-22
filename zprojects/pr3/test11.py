# pip install pydub

from pydub import AudioSegment
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

# Load the MP3 file
audio = AudioSegment.from_file((generate_filepath()+"example.mp3"), format="mp3")

# Get the duration in seconds
duration = audio.duration_seconds

# Print the duration
print("Duration:", duration, "seconds")
