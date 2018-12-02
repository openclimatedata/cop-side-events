import pandas as pd
import yaml
from requests_html import HTMLSession

agenda = []

session = HTMLSession()

url = "https://seors.unfccc.int/seors/reports/events_list.html?session_id=COP%2024"
r = session.get(url)

dateparse = lambda x: pd.datetime.strptime(x, "%d %b %Y").date()
timeparse = lambda x: pd.datetime.strptime(x, "%Y-%m-%d %H:%M")

table = r.html.find("table", containing="Monday", first=True)

items = table.find("tr")

events = []

for item in items:
    if "style" in item.attrs:
        fields = item.find("td")
        day = dateparse(fields[0].text.splitlines()[1])
        (time, location) = fields[1].text.splitlines()
        (start, end) = time.split("—")
        organiser = fields[2].text
        description = fields[3].text.strip()
        title = description.splitlines()[0]
        description = "\n".join(description.splitlines()[1:])
        links = list(fields[5].find("a"))
        if len(links) > 0:
            links = [{"text": link.text, "href": link.attrs["href"]} for link in links]
        print(day)
        print(start, end)
        print(location)
        print(title)
        print()
        print(description)
        print(links)
        event = {
            "day": day,
            "start": timeparse(f"{day} {start}"),
            "end": timeparse(f"{day} {end}"),
            "title": title,
            "location": location,
            "description": description,
            "links": links,
            "source": url,
        }
        events.append(event)
        print(40 * "=")

yaml.dump(events, open("unfccc.yaml", "w"), default_flow_style=False)
