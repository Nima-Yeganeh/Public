import wave
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

def get_mp3_duration(filename):
    with wave.open(filename, 'rb') as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration

# Example usage:
mp3_file = generate_filepath()+'example.mp3'
print(mp3_file)
duration = get_mp3_duration(mp3_file)
print(f"The duration of '{mp3_file}' is {duration:.2f} seconds.")
