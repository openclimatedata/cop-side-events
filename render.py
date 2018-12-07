import yaml
from slugify import slugify
from jinja2 import Environment, FileSystemLoader

template_loader = FileSystemLoader(searchpath="./")
env = Environment(extensions=["jinja2_time.TimeExtension"], loader=template_loader)
template = env.get_template("template.html")

sources = ["german.yaml", "unfccc.yaml", "wwf.yaml", "eu.yaml", "ndc.yaml", "brasil.yaml", "uk.yaml"]

events = []

for source in sources:
    data = yaml.load(open(source, "r"))
    events += data

events = sorted(events, key=lambda k: (k["start"], k["location"]))

for day in range(2, 15):
    for event in events:
        if event["start"].day == day:
            event["first"] = True
            break

for event in events:
    # Create Hash from location and start time, cutting of seconds.
    event["idx"] = slugify(f"{event['location']}-{event['start']}")[:-3]

with open("index.html", "w") as f:
    f.write(template.render(events=events))
