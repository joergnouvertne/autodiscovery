import time

from src.event_collector import EventCollector

events = EventCollector()

events.set_eventid()

testdict = {'oslevel': '12.01', 'version': 12, 'distribution': "SuSE Linux Enterprise Server 12"}

events.add_dict_event(testdict)

time.sleep(3)

events.add_string_event("Testevent with the same eventid but different timestamp")

events.unset_eventid()

events.set_timeformat("%c")

events.add_string_event("Testevent without eventid and local server timeformat")

events.set_eventid(event_id="bar", label="foo")

events.add_string_event("Testevent with static eventid")

events.set_eventid(time.strftime("%H%M%S"))

events.add_string_event("Testevent with time based dynamic eventid")

for event in events.eventlist:
    print event
