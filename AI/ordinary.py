import firebase_admin
import pdfkit
from firebase import firebase
from firebase_admin import credentials
from firebase_admin import db

import pdfkit


cred= credentials.Certificate('firebasesdk.json')


firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://medico-d0f60-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')

#
# data = {
#     'Patients': {
#         'p-1':{
#             'name': 'Souvik',
#             'dob': '24072004'
#         },
#         'p-2':{
#
#             'name': 'Rahul',
#             'dob': '08072004'
#         }
#     }
# }
#
#
# ref.set(data)



def searching_patients(name, dob):
    patientname= str(name)
    patientdob= str(dob)

    ref1 = db.reference('/Patients/')
    snapshot = ref1.get()

    if snapshot == None:
        return False
    elif snapshot!= None:

        namelist = []
        doblist = []

        for key, val in snapshot.items():
            ref2 = db.reference(f'/Patients/{key}/name')
            pname = ref2.get()
            namelist.append(pname)

            ref3 = db.reference(f'/Patients/{key}/dob')
            pdob = ref3.get()
            doblist.append(pdob)

        if patientname in namelist and patientdob in doblist:


            return True

        else:

            return False


def register_patient(name, dob, email, whatsapp, bloodgroup):

    try:

        ref0 = db.reference('/Patients/')
        snapshot = ref0.get()
        no_of_patient=0
        if snapshot == None:
            no_of_patient = 1

        elif snapshot!= None:
            keylist = []
            for key, val in snapshot.items():
                keylist.append(key)

            no_of_patient = len(keylist) + 1




        dataa = {
            f'p-{no_of_patient}': {
                'name': name,
                'dob': dob,
                'email': email,
                'whatsapp': whatsapp,
                'bloodgroup': bloodgroup
            }

        }
        ref0.update(dataa)
        return True

    except Exception as e:
        return False


# result5= register_patient('souvik', '5465450', 'bnvjdh', '5688', 'o')
#
# print(result5)









def patient_id(name, dob):
    patientname= str(name)
    patientdob= str(dob)

    ref1 = db.reference('/Patients/')
    snapshot = ref1.get()

    if snapshot == None:
        return False
    elif snapshot!= None:

        for key, val in snapshot.items():
            ref2 = db.reference(f'/Patients/{key}/name')
            pname = ref2.get()



            ref3 = db.reference(f'/Patients/{key}/dob')
            pdob = ref3.get()

            if pname == patientname and pdob == patientdob:

                detail= {
                    'patient name': pname,
                    'patient dob': pdob,
                    'patient phone': db.reference(f'/Patients/{key}/whatsapp').get(),
                    'patient email': db.reference(f'/Patients/{key}/email').get(),
                    'patient bloodgroup': db.reference(f'/Patients/{key}/bloodgroup').get(),
                    'patient id': key
                }

                return detail




