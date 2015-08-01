import schedule
import time
import smtplib

def send_email():
    gmail_user = "joyce_kim@berkeley.edu"
    gmail_pwd = "XXX"
    FROM = 'joyce_kim@berkeley.edu'
    TO = ['aniesha@citris-uc.org',
		'adriel_olmos@berkeley.edu',
		'alic.chen@citris-uc.org',
		'nonnecke@citris-uc.org',
		'charlenem@citris-uc.org',
		'cmartinez@citris-uc.org',
		'dan@citris-uc.org',
		'dlindeman@citris-uc.org',
		'dcaramag@citris-uc.org',
		'juliesammons@citris-uc.org',
		'karen@citris-uc.org',
		'khossrov@citris-uc.org',
		'pminor@citris-uc.org',
		'rmadison007@berkeley.edu',
		'therese.peffer@uc-ciee.org',
		'joyce_kim@berkeley.edu']  # must be a list
    SUBJECT = 'CBE Survey Reminder'
    TEXT = 'Dear All,' + '\n' + '\n' + 'Please take the survey now by clicking the link below.' + '\n' + '\n' + 'http://rightnow.cbe.berkeley.edu/survey/7DT1S/' + '\n' + '\n' + 'Thank you for your participation.' + '\n' + '\n' + 'Joyce'
    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        # server = smtplib.SMTP(SERVER)
        print 'connecting to gmail server'
        server = smtplib.SMTP("calmail.berkeley.edu", 587)  # or port 587 or 465 doesn't seem to work!
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        # server.quit()
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

# Mon
schedule.every().monday.at("10:00").do(send_email)
schedule.every().monday.at("13:30").do(send_email)
schedule.every().monday.at("15:30").do(send_email)
# Tues
schedule.every().tuesday.at("10:00").do(send_email)
schedule.every().tuesday.at("13:30").do(send_email)
schedule.every().tuesday.at("15:30").do(send_email)
# Wed
schedule.every().wednesday.at("10:00").do(send_email)
schedule.every().wednesday.at("13:30").do(send_email)
schedule.every().wednesday.at("15:30").do(send_email)
# Thur
schedule.every().thursday.at("10:00").do(send_email)
schedule.every().thursday.at("13:30").do(send_email)
schedule.every().thursday.at("15:30").do(send_email)
# Fri
schedule.every().friday.at("10:00").do(send_email)
schedule.every().friday.at("13:30").do(send_email)
schedule.every().friday.at("15:30").do(send_email)

while True:
    print "starting the script"
    schedule.run_pending()
    time.sleep(60)