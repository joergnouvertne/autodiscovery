import time
import datetime
import pytz
import re


class EventCollector:
    """
    Collect events in a list, enriched with an ISO 8601 compliant timestamp in UTC and the option to tag
    them with an event_id. The event_id can be used later in tools like Splunk to correlate
    events from the same scripts run.
    """

    def __init__(self):
        self.eventlist = []
        self.eventid = None

    def set_eventid(self, event_id='epochtime', label='event_id'):
        """
        Set an id for a set of events to correlate them in the event management tool

        :param label: The label of the identifier, default 'evid'
        :param event_id: A string which acts as an identifier, default is 'id=epochtimestamp utc'
        :return: self.eventid
        """
        if event_id == 'epochtime':
            self.eventid = label + "=" + self.epochtimestamp
        else:
            self.eventid = label + "=" + event_id

    def unset_eventid(self):
        """
        Remove eventid for the following events
        :return:
        """
        self.eventid = None

    @property
    def epochtimestamp(self):
        return str(int(time.mktime(datetime.datetime.now(tz=pytz.utc).timetuple())))

    @property
    def isotimestamp(self):
        return datetime.datetime.now(tz=pytz.utc).replace(microsecond=0).isoformat()

    def add_string_event(self, eventstring):
        """
        Add a string to the eventtlist, proceeded by the the current time and optionally the eventid
        """
        if self.eventid:
            self.eventlist.append(self.isotimestamp + ' ' + self.eventid + ' ' + eventstring)
        else:
            self.eventlist.append(self.isotimestamp + ' ' + eventstring)

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
