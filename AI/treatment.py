
import pyttsx3
import speech_recognition as sr
import firebase_admin

from firebase_admin import credentials
from firebase_admin import db

from datetime import date

from preescription_creator import make_prescription_pdf as mpp
from speaking import speak
from speaking import takecmnd
from googletrans import Translator


today = date.today()



cred = credentials.Certificate('firebasesdk.json')
try:
    firebase_admin.get_app()
except Exception as e:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://medico-d0f60-default-rtdb.firebaseio.com/'
    })






ref = db.reference('/')


translator= Translator()





def check_up(patient_id, name, dob):
    speak("ঠিক আছে এবার মেশিনের সামনে স্পষ্ট করে বলুন আপনার কি সমস্যা. উদাহরণ হিসেবে যদি আপনার খুব জ্বর হয়ে থাকে তো বলুন আমার খুব জ্বর?")
    problem= takecmnd().lower()
    speak('চিন্তা করবেন না, আমি আপনার সমস্যাটি শুনেছি এবং আমি আমার ডাটাবেসে কিছু সমাধানের সন্ধান করছি।আমাকে কিছু সময় দিন।')
    if 'fever' in problem:
        speak('আপনার সর্বাধিক কত জ্বর এসেছিলো যদি জানেন তো সেটা বলুন আর নাহলে বলুন জানিনা')
        highest_fever= takecmnd().lower()
        speak('আপনি কত দিন ধরে এই জ্বরে ভুগছেন?')
        suffering_days= takecmnd().lower()
        speak('আপনি কি আগে কোনো ওষুধ খেয়েছেন? যদি খেয়ে থাকেন তো বলুন হ্যাঁ আর নাহলে বলুন না.')
        reply= takecmnd().lower()
        prescription= {

            'medicine name': 'frequency',
            'calpol-650': 'twice in a day after breakfast and evening snacks',
            'clavam-625': 'once in a day after lunch',
            'payoz-40': 'twice in a day after breakfast and evening snacks'


        }

        ref1 = db.reference(f'/Patients/{patient_id}/prescrptions/{today}')
        ref1.update(prescription)
        arg= mpp(name,dob, 'High Fever', prescription)

        if arg is True:
            return True

        else:
            return arg




    else:
        return False