
import time
from io import BytesIO
import pygame
from gtts import gTTS
from googletrans import Translator
import speech_recognition as sr
from mutagen.mp3 import MP3
translator = Translator()
def speak(text):

    x = translator.detect(text).lang
    text1=''
    if 'bn' != x:
        text1 = translator.translate(text, dest='bn').text

    mp3_file_obj = BytesIO()
    tts= gTTS(text1, lang='bn')
    tts.write_to_fp(mp3_file_obj)
    pygame.init()
    pygame.mixer.init()
    mp3_file_obj.seek(0)
    pygame.mixer.music.load(mp3_file_obj, "mp3")
    song = MP3(mp3_file_obj)
    songLength = song.info.length
    pygame.mixer.music.play()
    time.sleep(songLength)

def takecmnd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

        try:
            print("I'm recognising...")
            request = translator.translate(r.recognize_google(audio), dest='en').text
            print(f"Boss:\t{translator.translate(request, dest='bn').text}\n")
        except Exception as e:
            print(e)
            speak("Please say that again")
            request = "sorry!!:("



        return request












