from smtplib import SMTP
import os

def send_email(user_email, user_height, average_height, entries):
    outlook = SMTP("smtp.office365.com", 587)
    outlook.starttls()
    outlook.login("heightcalculator@outlook.com", os.environ["EMAIL_PASSWORD"])
    outlook.sendmail("heightcalculator@outlook.com", user_email,
    "Subject:Average Height\n\nHi there,\nYour height is %scm"
    ",and the average height we recorded is %scm, out of %s entries.\n"
    "Thank you for submission." % (user_height, average_height, entries))
    outlook.quit()