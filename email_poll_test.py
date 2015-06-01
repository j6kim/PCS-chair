""" Example code sending automated emails based on smap metadata query.
    @ author Joyce Kim <joyce_kim@berkeley.edu>   joy
"""

from smap.archiver.client import SmapClient
from smap.contrib import dtutil

import time
import smtplib

def send_email(email_address):
    gmail_user = "ENTER SENDER EMAIL ADDRESS"
    gmail_pwd = "ENTER PSWD"
    FROM = 'ENTER SENDER EMAIL ADDRESS'
    TO = [email_address] #must be a list
    SUBJECT = "Testing sending using gmail"
    TEXT = "Testing sending mail using gmail servers"

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        #server = smtplib.SMTP(SERVER)
        server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        #server.quit()
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"


# make a client
c = SmapClient("http://www.openbms.org/backend")

while True:
    test = c.latest("Metadata/Extra/Type = 'oat'", 1, 10)
    if test[0]['Readings'][0][1] > 56:
        send_email("ENTER RECIPIENT EMAIL ADDRESS")
    time.sleep(10) # sleep for 10 sec

# example code - converting int to datetime
# dtutil.ts2dt(1357027200)
# dtutil.now()
# take date int & divide by 1000 since time is in miliseconds
