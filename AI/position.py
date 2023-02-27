# import pyautogui
import time

# 
# 
# x = pyautogui.position()
# print(x)
import gtts.lang
import pyttsx3
from io import BytesIO
import pygame
from gtts import gTTS
from googletrans import Translator
import speech_recognition as sr
from mutagen.mp3 import MP3






def speak(text):
    m= len(list(text))
    mp3_file_obj = BytesIO()
    tts= gTTS(text, lang='bn')
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
    recognizer = sr.Recognizer()
    translator = Translator()

    try:
        with sr.Microphone() as source:
            print('Speak Now')
            recognizer.adjust_for_ambient_noise(source)  # (Problem Solved)
            voice = recognizer.listen(source)
            text = recognizer.recognize_google(voice)
            print(text)

    except:
        pass

    translated = translator.translate(text, dest='en')
    print(translated.text)


mytext= 'khoma korben kichu jantrik trutir karone amra apnar chikitsa korte oparok, dya kore pore chesta korun.'
#





translator = Translator()
x= translator.translate(mytext, dest='bn')
print(x.text)
speak(x.text)






# save the pdf with name .pdf









