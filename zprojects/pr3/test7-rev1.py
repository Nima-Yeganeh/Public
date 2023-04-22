# python.exe -m pip install --upgrade pip
# pip install gtts
# pip3 install gtts
# pip install --upgrade gtts

from gtts import gTTS
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
