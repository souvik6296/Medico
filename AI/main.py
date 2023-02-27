import pyttsx3
import datetime
import speech_recognition as sr
import time
import webbrowser as wb
import pyautogui as pg
import keyboard

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

#print(voices)

engine.setProperty('voice', voices[1].id)





def speak(text):
    engine.say(text)
    engine.runAndWait()
    print(text)


def greed():
    hour= int(datetime.datetime.now().hour)

    if hour>=7 and hour<12:

        speak("Good morning boss")


    elif hour>=12 and hour<16:

        speak("Good noon boss")


    else:

        speak("Good evening boss")

    speak("I'm your test assistant AI")


def startactivitycmnd():
   while True:
       r = sr.Recognizer()
       with sr.Microphone() as source:
           print("Listening...")
           r.pause_threshold = 1
           r.energy_threshold = 200
           audio = r.listen(source)

           try:
               print("I'm listening...")
               request = r.recognize_google(audio, language='en-in')
               if request.lower() == "start listening":
                   speak("Listening started")
                   executor()




           except Exception as e:
               request = "sorry!!:("

           return request


def takecmnd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)

        try:
            print("I'm recognising...")
            request = r.recognize_google(audio, language='en-in')
            print(f"Boss:\t{request}\n")
        except Exception as e:
            print(e)
            speak("Please say that again")
            request = "sorry!!:("



        return request

def playsongfromYT():
    speak("Ok wait a while")
    # clicking chrome
    pg.click(x=651, y=755)
    time.sleep(7)
    # clicking on youtube
    pg.click(x=135, y=86)
    speak("Please say which music you want yo Listen")
    songname = takecmnd().lower()
    time.sleep(3)
    # clicking on searchbar
    pg.click(x=643, y=131)
    time.sleep(1)
    keyboard.write(songname)
    time.sleep(1)
    keyboard.press("enter")
    time.sleep(3)
    # clicking on music
    pg.click(x=481, y=326)
    speak("enjoy your song and say start listening when need again")
    startactivitycmnd()


def volumeset(volumelevel):

    # Get default audio device using PyCAW
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # Get current volume
#    currentVolumeDb = round(volume.GetMasterVolumeLevelScalar()*100)
    currentVolumeDb = volume.GetMasterVolumeLevelScalar()
    print(currentVolumeDb)
    volume.SetMasterVolumeLevelScaler(volumelevel/100)
    executor()



    # NOTE: -6.0 dB = half volume !

def executor():
    while True:
        speak("How may I help you")
        querry = takecmnd().lower()

        if querry == "can you hear me":
            speak("Yes")

        if "stop" in querry:
            speak("Ok Boss")
            startactivitycmnd()
            break

        if "play the music" in querry:
            playsongfromYT()
            break

        if "set volume" in querry:
            intence = int(querry.replace("set volume at ", ""))
            volumeset(intence)



if __name__ == '__main__':
    greed()

    executor()



