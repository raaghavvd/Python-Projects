from email.mime.text import MIMEText
import smtplib
def send_email(email,height,average_height,count):
    from_email="cena5729@gmail.com"
    from_password="jaisairam1995"
    to_email=email

    subject="Height Data"
    message="Hey there , your height is <strong>%s</strong> The average Height is <strong>%s</strong> from <strong>%s</strong>."% (height,average_height,count)
    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
