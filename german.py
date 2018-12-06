import pandas as pd
import yaml
from requests_html import HTML

agenda = []

with open("cache/german.html", "r") as f:
    r = HTML(html=f.read())

dateparse = lambda x: pd.datetime.strptime(x, "%Y %B %d").date()
timeparse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %H:%M")

events = r.find(".o-body__item.o-body__item--highlight")
for event in events:
    print(40 * "=")
    title = event.find("h2", first=True).text
    info = event.find("p")
    info = [x for x in info if len(x.text) > 0]
    if len(info) == 3:
        description = info[0].text
        organiser = info[1].text
        date = info[2].text
        day = dateparse("2018 " + date.split("|")[0].strip())
        time = date.split("|")[1].strip()
    elif len(info) == 2:
        organiser = info[0].text
        date = info[1].text
        day = dateparse("2018 " + date.split("|")[0].strip())
        time = date.split("|")[1].strip()
    elif title == "Welcoming Session":
        organiser = None
        date = "2018 December 2"
        day = dateparse("2018 December 2")
        time = info[0].text.strip()
    elif len(info) == 1:
        date = info[0].text
        day = dateparse("2018 " + date.split("|")[0].strip())
        time = date.split("|")[1].strip()
    if " - " in time:
        (start, end) = time.split(" - ")
        start = start.split(" ")[0].strip().replace(".", ":")
        end = end.split(" ")[0].strip().replace(".", ":")
    else:
        if " " in time:
            time = time.split(" ")[0]
        start = time.replace(".", ":")
        end = None
    if len(start) == 4:
        start = f"0{start}"
    start = timeparse(f"{day} {start}")
    if end:
        end = timeparse(f"{day} {end}")
    participants = event.find("ul", first=True)
    if participants:
        participants = participants.text.split("\n")
    links = event.find("a")
    if len(links) == 0:
        links = None
    else:
        links = [{"text": link.text, "href": link.attrs["href"]} for link in links]
    print(title)
    print(organiser)
    print(date)
    print(day)
    print(start)
    print(end)
    print(participants)
    print(links)

    info = {
        "title": title,
        "organiser": organiser,
        "start": start,
        "end": end,
        "participants": participants,
        "links": links,
        "location": "German Pavilion",
        "source": "https://www.bmu.de/en/german-climate-pavilion/events/",
    }
    agenda.append(info)
yaml.dump(agenda, open("german.yaml", "w"), default_flow_style=False)
