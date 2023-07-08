import smtplib
from email.message import EmailMessage
import imghdr


password ="****"
sender = "zazaovc44@gmail.com"
receiver = "statistiker74@gmail.com"
def send_email(image_path,):
    print("sendmail started")
    
    email_msg = EmailMessage()
    email_msg["Subject"] = "new person showed up"
    email_msg.set_content("Hey, Some one is here.")

    with open(image_path,'rb') as file:
        content = file.read()
    email_msg.add_attachment(content, mainType="image", subType=imghdr.what(None,content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver,email_msg.as_string())
    gmail.quit()
    print("sendmail ended")

    if __name__=="__main__":
        send_email(image_path='images/10.png')
