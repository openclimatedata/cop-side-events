import pandas as pd
import yaml
from requests_html import HTMLSession

agenda = []

session = HTMLSession()

url = "https://www.bmu.de/en/german-climate-pavilion/events/"
r = session.get(url)

dateparse = lambda x: pd.datetime.strptime(x, "%Y %B %d").date()
timeparse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %H:%M")

events = r.html.find(".o-body__item.o-body__item--highlight")
for event in events:
    print(40 * "=")
    title = event.find("h2", first=True).text
    info = event.find("p")
    if len(info) == 2:
        organiser = info[0].text
        date = info[1].text
        day = dateparse("2018 " + date.split("|")[0].strip())
        time = date.split("|")[1].strip()
    elif title == "Welcoming Session":
        organiser = None
        date = "2018 December 2"
        day = dateparse("2018 December 2")
        time = info[0].text.strip()
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
        "source": url,
    }
    agenda.append(info)
yaml.dump(agenda, open("german.yaml", "w"), default_flow_style=False)
