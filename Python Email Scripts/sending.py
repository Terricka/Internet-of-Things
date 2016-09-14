name = raw_input("Name of Email Recipient: ")
toemail = raw_input("What is their email address: ")
subjectline = raw_input("Subject: ")
textbody = raw_input("Body: ")
fromemail = raw_input("What is your email: ")


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = fromemail
toaddr = toemail
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subjectline
 
# body = textbody
msg.attach(MIMEText(textbody, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "*******")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()


success = "Your email was successfully sent to " + name + " at " + toemail + " from your email address: " + fromemail 

print success