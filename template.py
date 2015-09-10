import string
import dateutil.parser


class MailTemplate:

    def __init__(self, events, template="eventTemplate.html"):
        self.events = events
        self.template = template

    def new_message(self):

        events = self.events

        template = open('eventTemplate.html', "r", encoding="utf-8").read()

        event_list = []
        if not events:
            print('No upcoming events found.')
        for event in events:
            event_dict = dict()

            event_dict['start'] = event['start'].get('dateTime', event['start'].get('date'))
            event_dict['start'] = dateutil.parser.parse(event_dict['start']).strftime("%d %b %Y %H:%M:%S")

            event_dict['end'] = event['end'].get('dateTime', event['end'].get('date'))
            event_dict['end'] = dateutil.parser.parse(event_dict['end']).strftime("%d %b %Y %H:%M:%S")

            try:
                event_dict['description'] = event['description']
            except KeyError:
                event_dict['description'] = "Puudu"

            try:
                event_dict['summary'] = event['summary']
            except KeyError:
                event_dict['summary'] = "Puudu"

            try:
                event_dict['location'] = event['location']
            except KeyError:
                event_dict['location'] = "Teadmata"
            event_list.append(event_dict)

        tpl = string.Template(template)

        events2mail = []

        for event in event_list:
            events2mail.append(tpl.substitute(event))

        events_merged = ''.join(events2mail)
        return events_merged
