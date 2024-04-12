# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("new changes")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'pushing to master'
msg['From'] = 'xx@gmail.com'
msg['To'] = 'yy@gmail.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('smtp.gmail.com', 587)
s.send_message(msg)
s.quit()