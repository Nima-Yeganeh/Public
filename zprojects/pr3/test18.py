# pip install opencv-python-headless

import cv2
import os

def generate_filepath():
    original_string1 = __file__
    new_string1 = original_string1.replace(os.path.basename(__file__), '')
    newfile_path1 = new_string1
    return(newfile_path1)

input_file = generate_filepath()+'example.mp4'
output_file = generate_filepath()+'output.mp4'

# Open the input video file
cap = cv2.VideoCapture(input_file)

# Get the input video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the output video codec and writer
fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Process the frames and write to the output file
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        break

# Release the video file and writer objects
cap.release()
out.release()
