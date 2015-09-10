import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import config


class Mailer:

    def __init__(self, subject, body):
        self.subject = subject
        self.body = body

    def send_mail(self):
        from_addr = config.conf['fromEmail']
        to_addr = config.conf['toEmail']
        password = config.conf['password']

        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = self.subject

        body = self.body
        # plain may be more practical. But with html we could use more fancier template for newsletter.
        msg.attach(MIMEText(body, 'plain'))
        # msg.attach(MIMEText(body, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, password)
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()

