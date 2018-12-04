import pandas as pd
import yaml
from requests_html import HTML

agenda = []

with open("cache/wwf.html", "r") as f:
    r = HTML(html=f.read())

dateparse = lambda x: pd.datetime.strptime(x, "%d %b %Y").date()
timeparse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %H:%M")

agenda = []

columns = r.find(".col")

for col in columns:
    day = col.find("h2", first=True).text.split(" ", maxsplit=1)[1]
    day = dateparse(f"{day} 2018")
    events = col.find("div.event")
    for event in events:
        (title, organiser) = event.find("h3", first=True).text.splitlines()
        (start, end) = event.find("h4", first=True).text.split("-")
        start = timeparse(f"{day} {start}")
        end = timeparse(f"{day} {end}")
        description = event.find("p")[1].text
        speakers = [i.text for i in event.find("li")]
        print(day)
        print(start)
        print(end)

        print(title)
        print()
        print(description)
        print(organiser)
        print(speakers)
        print(40 * "=")

        item = {
            "start": start,
            "end": end,
            "title": title,
            "participants": speakers,
            "location": "WWF Pavilion",
            "description": description,
            "source": "https://wwf.panda.org/our_work/climate_and_energy/cop24/",
        }

        agenda.append(item)

yaml.dump(agenda, open("wwf.yaml", "w"), default_flow_style=False)
