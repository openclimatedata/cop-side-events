import pandas as pd
import yaml

events = []
dateparse = lambda x: pd.datetime.strptime(x, "%Y %d/%m").date()
def timeparse(x):
    if ":" in x:
        return pd.datetime.strptime(x, "%Y-%m-%d %I:%M%p")
    else:
        return pd.datetime.strptime(x, "%Y-%m-%d %I%p")

week1 = pd.read_html("cache/brasil-week-1.html")
assert len(week1) == 1
week1 = week1[0]
columns = week1.iloc[0]
week1 = week1.drop(5, axis=1)
week1.columns = columns.drop([1])
week1 = week1.drop([0, 1])
week1 = week1.set_index("WEEK 1")

for day in week1.columns:
    print("------")
    date = dateparse("2018 " + day.rsplit(" ")[-1])
    for time in week1.index:
        start, end = time.split(" – ")
        start = timeparse(f"{date.isoformat()} {start}")
        end = timeparse(f"{date.isoformat()} {end}")
        title = week1.loc[time, day]
        if title == "LUNCH":
            continue
        if not pd.isnull(title):
            events.append({
                "start": start,
                "end": end,
                "title": title,
                "location": "Brazilian Pavilion",
                "source": "http://espacobrasil.gov.br/en/brasil-pavilion/",
            })
            print(events[-1])

week2 = pd.read_html("cache/brasil-week-2.html")
assert len(week2) == 1
week2 = week2[0]
week2 = week2.drop(5, axis=1)
columns = week2.iloc[0]
week2.columns = columns
week2 = week2.drop([0, 1])
week2 = week2.set_index("WEEK 2")

for day in week2.columns:
    print("------")
    date = dateparse("2018 " + day.rsplit(" ")[-1])
    for time in week2.index:
        start, end = time.split(" – ")
        start = timeparse(f"{date.isoformat()} {start}")
        end = timeparse(f"{date.isoformat()} {end}")
        title = week2.loc[time, day]
        if not pd.isnull(title):
            events.append({
                "day": date,
                "start": start,
                "end": end,
                "title": title,
                "location": "Brazilian Pavilion",
                "source": "http://espacobrasil.gov.br/en/brasil-pavilion/",
            })
            print(events[-1])

yaml.dump(events, open("brasil.yaml", "w"), default_flow_style=False)
