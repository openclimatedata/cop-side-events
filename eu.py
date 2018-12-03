import pandas as pd
import yaml
import json


dateparse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d").date()
timeparse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %H:%M")

with open("schedule-rooms.json", "r") as f:
    schedule = json.load(f)

with open("eu-speakers.json", "r") as f:
    speakers = json.load(f)

with open("eu-organisers.json", "r") as f:
    organisers = json.load(f)


events = []

for key in schedule.keys():
    (date, location) = key.split(" ", maxsplit=1)
    print(date)
    print(location)

    #{'hourStart': '14:00',
    # 'hourEnd': '16:00',
    # 'type': 'None',
    # 'title': 'ACHIEVING HEALTH BENEFITS FROM CARBON REDUCTIONS',
    # 'organisers': [124],
    # 'speakers': [124],
    # 'details': '<p></p>',


    for event in schedule[key]:
        if "hourStart" not in event:
            continue

        orgs = "<br>".join([
            organisers[str(o)]["name"] for o in event["organisers"]
        ])
        participants = [
            speakers[str(s)]["name"] for s in event["speakers"]
        ]
        print(orgs)
        events.append({
            "day": dateparse(f"2018-{date}"),
            "start": timeparse(f"2018-{date} {event['hourStart']}"),
            "end": timeparse(f"2018-{date} {event['hourEnd']}"),
            "title": event["title"],
            "description": event["details"],
            "location": f"EU Pavilion {location}",
            "source": "http://ec.europa.eu/clima/events/0124/calendar_en.htm#schedule",
            "organiser": orgs,
            "participants": participants
        })
    print(events[-1])


yaml.dump(events, open("eu.yaml", "w"), default_flow_style=False)
