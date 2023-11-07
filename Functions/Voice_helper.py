
from gtts import gTTS
from pygame import mixer
import time

def voice(text, lang='ru'):
    file = text
    mp3_name = "xyi.mp3"
    tts = gTTS(text=file, lang=lang,)
    tts.save(mp3_name)


    mixer.init()
    mixer.music.load(mp3_name)
    mixer.music.play()
    #time.sleep(len(file))


