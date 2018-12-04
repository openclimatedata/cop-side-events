import pandas as pd
import yaml

events = []
timeparse = lambda x: pd.datetime.strptime(x, "%Y %A %d %B %H:%M")

with open("cache/uk.html", 'r') as f:
    html = f.read().replace("<br>", '####').replace("<br />", "####")

table = pd.read_html(html)[0]
table.columns = table.loc[0]
table = table.drop(0)

def remove_topic(time):
    # e.g. 'Thursday 13th December – Energy Transitions'
    if "December" in time:
        return time.split(" – ")[0]
    else:
        return time

table.Time = table.Time.apply(remove_topic)

for item in table.iterrows():
    if "December" in item[1].Time:
        day = item[1].Time.strip()
    if ":" in item[1].Time:
        (start, end) = item[1].Time.split("-")
        start = start.strip()
        end = end.strip()
        print(item[1].Time)
        start = timeparse(f"2018 {day} {start}".replace("th ", " ").replace("rd\xa0", " "))
        if end.lower() == "close":
            end = None
        else:
            end = timeparse(f"2018 {day} {end}".replace("th ", " ").replace("rd\xa0", " "))
        try:
            (title, description) = item[1].Event.split("####", maxsplit=1)
            title = title.strip()
            description = description.strip().replace("####", "<br>")
        except ValueError:
            title = item[1].Event
            description = None
        if pd.isnull(item[1].Organisation):
            organiser = None
        else:
            organiser = item[1].Organisation.replace("####", '<br>')
        events.append({
            "day": start.date(),
            "start": start,
            "end": end,
            "title": title,
            "description": description,
            "organiser": organiser,
            "location": "UK Pavilion",
            "source": "https://www.events.great.gov.uk/ehome/index.php?eventid=200184147",
        })
        print(events[-1])

yaml.dump(events, open("uk.yaml", "w"), default_flow_style=False)
