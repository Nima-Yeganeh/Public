# pip install ffmpeg-python

import ffmpeg
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

input_file = generate_filepath()+'example.mp4'
output_file = generate_filepath()+'output.mp4'
print(input_file)
print(output_file)

# Define the input stream
input_stream = ffmpeg.input(input_file)

# Convert the video codec to H.264/AVC
output_stream = ffmpeg.output(input_stream, output_file, vcodec='libx264')

# Run the FFmpeg command
ffmpeg.run(output_stream)
