
import fpdf
from datetime import date
from send_mail import send_mail
from ordinary import patient_id
from pathlib import Path
import time
import os

pdf= fpdf.FPDF()
today = date.today()


prescription= {

            'calpol-650': 'twice in a day after breakfast and evening snacks',
            'clavam-625': 'once in a day after lunch',
            'payoz-40': 'twice in a day after breakfast and evening snacks'


        }

def get_range(p):
    list1 = []
    for key in p:
        list1.append(key)

    return len(list1)


def make_prescription_pdf(patientname, dob, issue, prescription):
    # Add a page
    pdf.add_page()

    # set style and size of font for Heading

    pdf.set_font("Arial", size=30, style='BU')

    # create a heading cell
    pdf.set_fill_color(255, 255, 0)

    pdf.cell(200, 10, txt="MEDICO an A.I. based medical bot",
             ln=1, align='C', fill=True)

    # set style and size of font for body


    # patient detail cell
    pdf.set_font("Arial", size=17)
    pdf.cell(200, 10, txt=f'Patient name: {patientname}',
             ln=2, align='L')
    pdf.set_font("Arial", size=17)
    pdf.cell(200, 10, txt=f'Date: {today}',
             ln=3, align='L')
    pdf.set_font("Arial", size=17)
    pdf.cell(200, 10, txt=f'Issue:\t{issue}',
             ln=4, align='L')
    pdf.set_font("Arial", size=20)
    pdf.set_font("Arial", size=15, style='BU')
    pdf.cell(200, 10, txt=f'Medicines to be taken and time to take:',
             ln=5, align='C')

    i = 0
    range1 = get_range(prescription)
    for key in prescription:
        if i <= range1:
            pdf.set_font("Arial", size=15)
            pdf.cell(200, 10, txt=f'{key}\t----->\t{prescription[key]}',
                     ln=7 + i, align='C')
            i += 1

    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f'Thanking You,',
             ln=10 + i, align='R')

    prescription_name = f"prescripion_({today}).pdf"

    pdf.output(prescription_name)

    email = patient_id(patientname, dob)['patient email']

    path = Path(f'./{prescription_name}')
    result = None
    while True:
        x = path.is_file()
        if x is True:
            result = send_mail(prescription_name, patientname, email)
            break

        elif x is False:
            time.sleep(5)

    if result is True:
        os.remove(path)
        return True
    elif result is False:
        return False

    else:
        return 'problem is here'




#make_prescription_pdf('Souvik',24072004,'High fever',prescription)