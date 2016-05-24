from event_collector import EventCollector
from osinfo import OSInfo

events = EventCollector()
events.set_eventid()

server = OSInfo()

events.add_dict_event(server.get_info)

for event in events.eventlist:
    print event
