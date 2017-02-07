import smtplib
content = "python test mail"

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('vivek.ku.mohanty@gmail.com','password')

mail.sendmail('vivek.ku.mohanty@gmail.com','vivek.kumohanty@yahoo.com',content)

mail.close()
