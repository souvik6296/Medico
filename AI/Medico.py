


from ordinary import searching_patients as sp
from ordinary import register_patient as rp
from ordinary import patient_id as pd
from treatment import check_up as cu
from speaking import takecmnd
from speaking import speak











def register_patient(name, dob):

    email= ''
    whatsapp= ''
    blood_group= ''

    speak('যদি আপনি আপনার ইমেইল জানেন তো সেটা বলেন নাহলে বলুন জানিনা. মনে রাখবেন আপনার প্রেসক্রিপশন পাঠানোর ক্ষেত্রে আপনার ইমেইল টি খুবই গুরুত্বপূর্ণ')
    response2 = takecmnd().lower()
    if 'dont know' in response2:
        email= 'unknown'

    else:
        email=response2

    speak('যদি আপনি স্বচ্ছন্দ বোধ করেন তো আপনার হোয়াটস্যাপ নম্বর তা বলুন আর নাহলে বলুন জানিনা. মনে রাখবেন ইটা শুধুমাত্র প্রেসক্রিপশন পাঠানো বা কোনো আপডেট পাঠানোর জন্য.')
    responnse = takecmnd().lower()
    if 'dont know' in responnse:
        whatsapp=0000

    else:
        whatsapp=int(responnse)

    speak('আপনার রক্তের গ্রুপ জানা থাকলে বলুন নাহলে বলুন জানিনা')
    responnse1 = takecmnd().lower()

    if 'dont know' in responnse1:
        blood_group= 'unknown'

    else:
        blood_group=responnse1

    speak("আমি আপনার দেওয়া তথ্য আমাদের ডাটাবেস এ সংরক্ষন করছি, দয়া করে কিছুক্ষন অপেক্ষা করুন")
    result= rp(name, dob, email, whatsapp, blood_group)

    if result is True:
        speak('অভিনন্দন! আপনি সফলভাবে রেজিস্টার্ড হয়েছেন')
        return True


    if result is False:
        speak('দুঃখিত আমরা আপনার দেওয়া তথ্য জমা করতে অসফল হয়েছি. অনুগ্রহ করে পরে চেষ্টা করুন')
        return False





def executor():
    while True:
        #speak("How may I help you")
        querry = input('plz write')#takecmnd().lower()

        if "medico" in querry:
            speak('স্বাগতম! আমি মেডিকো. দয়া করে আপনার নাম টি বলুন')
            name= takecmnd().lower()
            speak('দয়া করে আপনার জন্ম তারিখটি ডি ডি এম এম ওয়াই ওয়াই ওয়াই ফর্ম্যাটে ধীরে ধীরে বলুন')
            dateofbirth= input('plz write')#takecmnd().lower()

            registered = sp(name, dateofbirth)
            if registered is True:
                speak('আপনি একজন রেজিস্টার্ড রোগী')
                patient_id=pd(name, dateofbirth)['patient id']
                treatment_done = cu(patient_id, name, dateofbirth)
                if treatment_done is True:
                    speak('আপনার চিকিৎসা সম্পূর্ণ হয়েছে এবং আপনার প্রেসক্রিপশন পিডিএফ ফাইল হিসেবে মেইল করে দেওয়া হয়েছে. মেডিকো আপনাকে জানাই অনেক অনেক ধন্যবাদ, আপনার দিন শুভ হোক')
                    print('done')
                    break
                else:
                    speak('ক্ষমা করবেন কিছু যান্ত্রিক ত্রুটির কারণে আমরা আপনার চিকিৎসা করতে অপারক, দয়া করে পরে চেষ্টা করুন.')


            if registered is False:
                speak('আপনি একজন রেজিস্টার্ড রোগী নন. আপনি কি রেজিস্টার্ড করতে চান নাকি অতিথি হিসেবে চালিয়ে যেতে চান?')
                querry = takecmnd().lower()
                if "register" in querry:
                    response= register_patient(name, dateofbirth)
                    if response is True:
                        patient_id = pd(name, dateofbirth)['patient id']
                        treatment_done = cu(patient_id, name, dateofbirth)
                        if treatment_done is True:
                            speak(
                                'আপনার চিকিৎসা সম্পূর্ণ হয়েছে এবং আপনার প্রেসক্রিপশন পিডিএফ ফাইল হিসেবে মেইল করে দেওয়া হয়েছে. মেডিকো আপনাকে জানাই অনেক অনেক ধন্যবাদ, আপনার দিন শুভ হোক')
                            print('done')
                            break
                        else:
                            speak('ক্ষমা করবেন কিছু যান্ত্রিক ত্রুটির কারণে আমরা আপনার চিকিৎসা করতে অপারক, দয়া করে পরে চেষ্টা করুন.')
                        print('continue')
                        break

                    if response is False:
                        speak(
                            'ক্ষমা করবেন কিছু যান্ত্রিক ত্রুটির কারণে আমরা আপনার চিকিৎসা করতে অপারক, দয়া করে পরে চেষ্টা করুন.')
                        print('problem')
                        break

                if "guest" in querry:
                    break




if __name__ == '__main__':

    executor()
