import os 
from gtts import gTTS
import tempfile


filepath = "/home/hello-robot/smarthome_ws/src/smart-home-robot/shr_resources/resources/am_med_reminder.txt"
def create_mp4_from_text(file_path):
        (mp4file, mp4filename) = tempfile.mkstemp(
                prefix='sound_play', suffix='.mp4')

        # Create a gTTS object with the text and language
        with open(file_path, 'r') as f:
                mytext = f.read()
        tts_obj = gTTS(text=mytext, lang='en', slow=False)

        # Save the generated speech as an MP4 file
        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as f:
                mp4filename = f.name
                tts_obj.save(mp4filename)

        return mp4filename

wavfilename = create_mp4_from_text(filepath)
os.system('mpg321 ' + wavfilename)