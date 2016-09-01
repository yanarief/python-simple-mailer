#!/usr/bin/python
# please setup sender account
# please file receipe meet you need

import time
import smtplib
import csv
import sys
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import email.utils

data = open('accountlist.csv')
csvFile = csv.reader(data)
mailfrom = "Saya <my@domain.com>"
for row in csvFile:
    rcptname = str(row[0]) + " " + str(row[1])
    lampiran="/path/to/attch2/FileNameSameAsRcptName-"+str(row[0]) + str(row[1]) + ".pdf"
    mailto = str(row[2])
    contentFile = open('mymessage.txt', 'r')
    msg = MIMEMultipart()
    msg['From'] = mailfrom
    msg['Date'] = email.utils.formatdate(localtime=True)
    msg['To'] = rcptname + " <" + mailto + ">"
    msg['Subject'] = "Subyek Email"
    msg.attach(MIMEText( "Dear "+ rcptname + ",\n\n" + contentFile.read() ))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(lampiran, "rb").read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename="FileNameSameAsRcptName-"+str(row[0]) + str(row[1]) + ".pdf")
    msg.attach(part)

    server = smtplib.SMTP('mail.domain.com', 587)
    server.starttls()
    server.ehlo()
    server.login("my@domain.com", "mypassword")
    try:
        server.sendmail(mailfrom, mailto, msg.as_string())
        server.quit()
        print time.strftime("%Y-%m-%d %H:%M:%S") + " - Berhasil mengirim ke "+ msg['To']
        time.sleep(3)
    except SMTPException:
        print "Gagal mengirim email"
        server.quit()
