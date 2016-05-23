import time
import re


class EventCollector:
    """
    Collect events in a list, enriched wit ha predefined timestamp and the option to tag
    them with an event_id. The event_id can be used later in tools like Splunk to correlate
    events from the same scripts run.
    """

    def __init__(self):
        self.eventlist = []
        self.eventid = None
        self.timeformat = "%Y-%m-%dT%H:%M:%S%z"

    def set_eventid(self, event_id='epochtime', label='event_id'):
        """
        Set an id for a set of events to correlate them in the event management tool

        :param label: The label of the identifier, default 'evid'
        :param event_id: A string which acts as an identifier, default is 'id=epochtimestamp'
        :return: self.eventid
        """
        if event_id == 'epochtime':
            self.eventid = label + "=" + str(int(time.time()))
        else:
            self.eventid = label + "=" + event_id

    def unset_eventid(self):
        """
        Remove eventid for the following events
        :return:
        """
        self.eventid = None

    def set_timeformat(self, timeformat):
        """
        Set the format of the timestamp of each evnt
        :param timeformat: String used by the time.strftime() function
        :return: self.timeformat
        """
        try:
            time.strftime(timeformat)
            self.timeformat = timeformat
        except:
            raise TypeError

    def add_string_event(self, eventstring):
        """
        Add a string to the eventtlist, proceeded by the the current time and optionally the eventid
        """
        if self.eventid:
            self.eventlist.append(time.strftime(self.timeformat) + ' ' + self.eventid + ' ' + eventstring)
        else:
            self.eventlist.append(time.strftime(self.timeformat) + ' ' + eventstring)

    def add_dict_event(self, event_dict):
        """
        Convert a flat dict object into an key=value based event
        :param event_dict:
        :return:
        """
        eventstring = ''
        for kvpair in event_dict:
            if re.search(r"\s", str(event_dict[kvpair])):
                eventstring += '  ' + kvpair + '="' + str(event_dict[kvpair]) + '"'
            else:
                eventstring += '  ' + kvpair + '=' + str(event_dict[kvpair])
        eventstring = eventstring.strip()
        self.add_string_event(eventstring)
