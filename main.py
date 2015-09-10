import datetime
from apiclient import discovery
import template
import config
from sendMail import Mailer

if __name__ == '__main__':
    service = discovery.build('calendar', 'v3', developerKey=config.conf['apiKey'])

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    endDate = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    endDate = endDate.isoformat() + 'Z'

    print('Getting the upcoming events from ', now, 'to ', endDate)
    eventsResult = service.events().list(
        calendarId=config.conf['calendarId'], timeMin=now, timeMax=endDate, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    print("Number of events found : ", len(events))

    mailMessage = template.MailTemplate(events)
    newMail = Mailer("Nädala sõnumid", mailMessage.new_message())
    newMail.send_mail()






