from moviepy.editor import VideoFileClip
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

input_file = generate_filepath()+'example.mp4'
output_file = generate_filepath()+'output.mp4'

# Load the input video clip
clip = VideoFileClip(input_file)

# Write the output video file with the H.264/AVC codec
clip.write_videofile(output_file, codec='libx264')

# Close the video clip object
clip.close()
