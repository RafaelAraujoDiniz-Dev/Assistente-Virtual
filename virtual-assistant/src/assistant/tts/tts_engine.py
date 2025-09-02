from gtts import gTTS
import os

class TTS:
    def __init__(self, language='en'):
        self.language = language

    def speak(self, text):
        tts = gTTS(text=text, lang=self.language, slow=False)
        audio_file = 'temp_audio.mp3'
        tts.save(audio_file)
        os.system(f'start {audio_file}')  # For Windows, use 'start', for Mac use 'afplay', for Linux use 'xdg-open'

    def set_language(self, language):
        self.language = language

    def get_language(self):
        return self.language