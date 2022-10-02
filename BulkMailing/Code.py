from email.message import EmailMessage
import smtplib
import email

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('Your_email_id', 'Your_email_id_app_password')#Before running the program you should update the code with your email id and its password
print("Welcome To Your Own Mail system\nSend messages to all")
msg = EmailMessage()
msg['From'] = 'Your_email_id'#update with your email id

text_f = open('data.txt', 'r')# Add the email id of recipient in the data.txt folder befroe running the program.
data = text_f.read()
text_f.close()
mails = list(data.split(","))
msg['Subject'] = input("Enter the subject\n")
msg.set_content(input("Enter the message\n"))
for mail in mails:
    msg['To'] = mail
    server.send_message(msg)
    del msg['To']
print("Mail sent to all")
