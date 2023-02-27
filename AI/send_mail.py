from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import datetime
today= datetime.date.today()
import os
from pathlib import Path
import time
def send_mail(pdfname, recievername, receiver):


    while True:
        path = Path(f'./{pdfname}')

        if path.is_file() is True:
            try:
                body = f'''Hello,
                This is a mail from Medico. 
                Your Prescription is attached at down as pdf file.
                Dowwnload it.
                Thank You.
                Patient name: {recievername}
                Date: {today}
                '''

                sender = 'souvikgupta64@gmail.com'
                password = 'svugkgtfxwmsownx'

                # Setup the MIME
                message = MIMEMultipart()
                message['From'] = sender
                message['To'] = receiver
                message['Subject'] = pdfname

                message.attach(MIMEText(body, 'plain'))

                # open the file in bynary
                binary_pdf = open(pdfname, 'rb')

                payload = MIMEBase('application', 'octate-stream', Name=pdfname)
                payload.set_payload((binary_pdf).read())

                # enconding the binary into base64
                encoders.encode_base64(payload)

                # add header with pdf name
                payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
                message.attach(payload)

                # use gmail with port
                session = smtplib.SMTP('smtp.gmail.com', 587)

                # enable security
                session.starttls()

                # login with mail_id and password
                session.login(sender, password)

                text = message.as_string()
                session.sendmail(sender, receiver, text)
                session.quit()
                print('Mail Sent')
                os.remove(f'.{pdfname}')
                return True



            except Exception as e:
                return False


        elif path.is_file() is False:
            time.sleep(5)



