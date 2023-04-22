import subprocess
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

input_file = generate_filepath()+'example.mp4'
output_file = generate_filepath()+'output.mp4'

# Run FFmpeg command to convert the video
subprocess.run(['ffmpeg', '-i', input_file, '-c:v', 'libx264', '-crf', '23', '-preset', 'medium', '-c:a', 'copy', output_file], check=True)

print('Conversion complete.')
