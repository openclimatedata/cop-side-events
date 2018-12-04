import yaml
from ics import Calendar

output = []
for filename in ["ndc-calendar-w1.ics", "ndc-calendar-w2.ics"]:

    calendar = Calendar(open(filename, "r"))

    events = calendar.events


    for event in events:
        if event.all_day:
            continue

        if event.location == "NDC Partnership Pavillion, Hall E, Pavillion #22, Poland" or event.location is None:
            location = "NDC Partnership Pavilion"
        else:
            location = "NDC Partnership: " + event.location

        output.append({
            "title": event.name,
            "description": event.description.strip(),
            "start": event.begin.datetime,
            "end": event.end.datetime,
            "source": "http://www.ndcpartnershipcop.org/events/",
            "location": location,
        })
        print(output[-1])

yaml.dump(output, open("ndc.yaml", "w"), default_flow_style=False)
