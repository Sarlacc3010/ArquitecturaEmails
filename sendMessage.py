import ssl
from email.message import EmailMessage
import smtplib
import time

email_sender = 'carlozedmusa@gmail.com'       # Ingresar mail desde donde se enviaran los mensajes
email_password = ''     # Ingresar contraseña del email
email_receiver = 'carlozedmusa@gmail.com'     # Ingresar email que recibira los mensajes

subject = 'Check email send'
body = """
Mensaje de prueba
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

x = 1
while x < 10:

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    x += 1
    time.sleep(10)
