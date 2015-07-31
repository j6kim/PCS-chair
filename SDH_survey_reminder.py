import schedule
import time
import smtplib

def send_email():
    gmail_user = "cbe.surveys@gmail.com"
    gmail_pwd = "390wurster"
    FROM = 'cbe.surveys@gmail.com'
    TO = ['joyce_kim@berkeley.edu',
          'joycekim.jh@gmail.com']  # must be a list
    SUBJECT = 'CBE Survey Reminder'
    TEXT = 'Dear All,' + '\n' + '\n' + 'Please take the survey now by clicking the link below.' + '\n' + '\n' + 'http://rightnow.cbe.berkeley.edu/survey/7DT1S/' + '\n' + '\n' + 'Thank you for your participation.' + '\n' + '\n' + 'Joyce'
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        # server = smtplib.SMTP(SERVER)
        print 'connecting to gmail server'
        server = smtplib.SMTP("smtp.gmail.com", 587)  # or port 587 or 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        # server.quit()
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

schedule.every().day.at("16:18").do(send_email)
schedule.every().day.at("16:19").do(send_email)
schedule.every().day.at("16:20").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(30)