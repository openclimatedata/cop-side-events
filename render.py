import yaml
from jinja2 import Environment

env = Environment(extensions=["jinja2_time.TimeExtension"])

sources = ["german.yaml", "unfccc.yaml", "wwf.yaml", "eu.yaml", "ndc.yaml"]

events = []

for source in sources:
    data = yaml.load(open(source, "r"))
    events += data

events = sorted(events, key=lambda k: (k["start"], k["location"]))

for day in range(2, 15):
    for event in events:
        if event["day"].day == day:
            event["first"] = True
            break

template = env.from_string(
    """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>(Unoffical) #COP24 Side Events Tracker</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css">
    <style>
      .container {
        max-width: 768px;
      }
      .section {
        padding: 0 1rem 0 1rem;
      }
      a.anchor {
        display:block;
        padding-top: 110px;
        margin-top: -110px;
      }
    </style>
  </head>
  <body class="has-navbar-fixed-top">
  <nav class="navbar is-fixed-top is-dark" role="navigation" aria-label="main navigation dropdown">
  <div class="navbar-brand">
    <a class="navbar-item" href="#">
      #COP24&nbsp;<span class="is-hidden-mobile"> (Unofficial) Side Event Tracker</span>
    </a>

    <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbar-rest">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div class="navbar-menu" id="navbar-rest">
    <div class="navbar-start">
      <span class="navbar-item is-hidden-touch">December</span>
      <a class="navbar-item" id="dec02" href="#02"><span class="is-hidden-desktop">December </span>2nd</a>
      <a class="navbar-item" id="dec03" href="#03"><span class="is-hidden-desktop">December </span>3rd</a>
      <a class="navbar-item" id="dec04" href="#04"><span class="is-hidden-desktop">December </span>4th</a>
      <a class="navbar-item" id="dec05" href="#05"><span class="is-hidden-desktop">December </span>5th</a>
      <a class="navbar-item" id="dec06" href="#06"><span class="is-hidden-desktop">December </span>6th</a>
      <a class="navbar-item" id="dec07" href="#07"><span class="is-hidden-desktop">December </span>7th</a>
      <a class="navbar-item" id="dec08" href="#08"><span class="is-hidden-desktop">December </span>8th</a>
      <a class="navbar-item" id="dec10" href="#10"><span class="is-hidden-desktop">December </span>10th</a>
      <a class="navbar-item" id="dec11" href="#11"><span class="is-hidden-desktop">December </span>11th</a>
      <a class="navbar-item" id="dec12" href="#12"><span class="is-hidden-desktop">December </span>12th</a>
      <a class="navbar-item" id="dec13" href="#13"><span class="is-hidden-desktop">December </span>13th</a>
      <a class="navbar-item" id="dec14" href="#14"><span class="is-hidden-desktop">December </span>14th</a>
    </div>
    <div class="navbar-end">
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">More Side Events</a>
        <div class="navbar-dropdown">
          <a href="https://unfccc.int/climate-action/events/global-climate-action-at-cop24/action-hub-events" class="navbar-item">Climate Action Hub</a>
          <a href="https://unfccc.int/climate-action/events/global-climate-action-events-at-cop24-full-programme-including-action-hub" class="navbar-item">Global Climate Action Events</a>
          <a href="https://unfccc.int/climate-action/marrakech-partnership/events/marrakech-partnership-at-cop24" class="navbar-item">Marrakech Partnership</a>
          <hr class="navbar-divider">
          <a href="https://www.ccca.ac.at/en/dialog-fields/cop24/" class="navbar-item">Austrian Pavilion</a>
          <a href="https://www.greenclimate.fund/cop" class="navbar-item">Green Climate Fund Pavilion</a>
          <a href="http://indonesiaunfccc.com/" class="navbar-item">Indonesian Pavilion</a>
          <a href="http://www.ndcpartnershipcop.org/events/week/2018-12-03/?tribe_event_display=week&tribe-bar-date=2018-12-03" class="navbar-item">NDC Partnership</a>
          <a href="http://copjapan.env.go.jp/cop/cop24/en/events/" class="navbar-item">Japanese Pavilion</a>
          <a href="https://ipcc.ch/apps/outreach/eventinfo.php?q=446" class="navbar-item">IPCC Events</a>
          <a href="http://cop24.gov.pl/conference/agenda/polish-pavilion/" class="navbar-item">Polish Pavilion</a>
          <a href="https://cop23.com.fj/cop24/cop24-pacific-koronivia-pavilion/" class="navbar-item">Pacific and Koronivia Pavilion</a>
          <a href="https://www.worldbank.org/en/events/2018/11/30/mdb-joint-pavilion-at-cop24" class="navbar-item">Multilateral Development Banks Pavilion</a>
          <hr class="navbar-divider">
          <a href="http://www.undp.org/content/undp/en/home/events/2018/climate-2020/cop24.html" class="navbar-item">UNDP Events</a>
          <a href="http://www.oecd.org/environment/cc/cop24/" class="navbar-item">OECD Events</a>
          <a href="https://www.wri.org/events/2018/12/wri-events-cop24" class="navbar-item">WRI Events</a>
          <hr class="navbar-divider">
          <a href="https://unfccc.int/process-and-meetings/conferences/katowice-climate-change-conference-december-2018/events-and-schedules/pavilions-at-cop-24" class="navbar-item">UNFCCC Information</a>
        </div>
      </div>
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">Sources</a>
        <div class="navbar-dropdown">
          <a href="https://seors.unfccc.int/seors/reports/events_list.html?session_id=COP%2024" class="navbar-item">UNFCCC Side Events</a>
          <a  href="http://ec.europa.eu/clima/events/0124/calendar_en.htm#schedule" class="navbar-item">EU Pavilion</a>
          <a href="https://www.bmu.de/en/german-climate-pavilion/events/" class="navbar-item">German Pavilion</a>
          <a href="https://wwf.panda.org/our_work/climate_and_energy/cop24/" class="navbar-item">WWF Pavilion</a>
        </div>
      </div>
      <a href="https://twitter.com/openclimatedata" class="navbar-item">Made by  @openclimatedata</a>
    </div>
  </div>
  </nav>
  <div class="container">
    <section class="section content">
    <p>
    Last Update: {% now 'Europe/Berlin', '%a, %d %b %Y %H:%M' %}<br>
    Please always check with the linked original schedule for latest changes.<br>
    Made by <a href="mailto:robert.gieseke@pik-potsdam.de">Robert Gieseke</a><br>
    Source code on <a href="https://github.com/openclimatedata/cop-side-events">GitHub</a><br>
    Follow me on Twitter: <a href="https://twitter.com/openclimatedata">@openclimatedata</a>
    </p>
    <p>
    Venue Map: <a href="https://unfccc.int/sites/default/files/resource/COP24%20-%20All%20Areas%20-%2016_FINAL.pdf">All - Areas - 16_FINAL.pdf</a><br>
    </p>
    <p>
    <a class="button is-primary" id="togglePastEvents"><span id="show" class="showOrHide is-hidden">Show</span><span id="hide" class="showOrHide">Hide</span>&nbsp;past events</a>
    </p>
    </section>
    {% for event in events %}
      {% if event["first"] %}<a id="{{ event.day.strftime("%d") }}" class="anchor"></a>{% endif %}
      <section class="section is-size-6 is-size-7-touch">
      <p class="is-size-5 is-size-6-touch">{{ event.day.strftime('%A, %d %B') }}<br>
      <time datetime="{{ event.start.strftime("%Y-%m-%d %H:%M") }}">{{ event.start.strftime("%H:%M") }}</time> -
      {% if event.end %}
        {{ event.end.strftime("%H:%M") }}
      {% endif %}
      </p>
      <h2 class="is-size-4 is-size-5-touch"><a class="has-text-primary" href="{{ event.source }}">{{ event.location }}</a><br> {{ event.title }}</h2>
      {% if event.description %}
        <p>{{ event.description }}</p>
      {% endif %}
      {% if event.organiser %}
        <p>{{ event.organiser }}</p>
      {% endif %}
      {% if event.participants %}
        <h4 class="has-text-weight-bold">Speakers</h4>
        <ul>
          {% for participant in event.participants %}
            <li>{{ participant }}</li>
          {% endfor %}
        </ul>
      {% endif %}
      {% if event.links %}
        <p>
        <h4 class="has-text-weight-bold">Links</h4>
        {% for link in event.links %}
          <a href="{{ link.href }}">{{ link.text }}</a><br>
        {% endfor %}
        </p>
      {% endif %}
      <hr>
      </section>
    {% endfor %}
  </div>
  <script>
    var now = new Date()
    var addZero = function(i) {
        if (i < 10) {
            i = "0" + i
        }
        return i
    }
    var nowString = now.getFullYear() + "-" + addZero((now.getMonth()+1)) + '-' + addZero(now.getDate()) + ' ' + addZero(now.getHours() - 1) + ":" + addZero(now.getMinutes() - 30)
    var times = document.getElementsByTagName("time")
    var togglePastEvents = function() {
        for (var i = 0; i < times.length; i++) {
            if (times[i].attributes["datetime"].value < nowString) {
              times[i].parentElement.parentElement.classList.toggle("is-hidden")
            }
        }
        [].slice.call(document.getElementsByClassName("showOrHide"))
            .forEach(function(el) {
                el.classList.toggle("is-hidden")
            })

    }
    togglePastEvents()

    // Get all "navbar-burger" elements
    var $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

    // Check if there are any navbar burgers
    if ($navbarBurgers.length > 0) {

    // Add a click event on each of them
    $navbarBurgers.forEach( function(el) {
      el.addEventListener('click', function() {

        // Get the target from the "data-target" attribute
        var target = el.dataset.target;
        var $target = document.getElementById(target);

        // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
        el.classList.toggle('is-active')
        $target.classList.toggle('is-active')
      });
    });
    }

    var $rest = document.getElementById("navbar-rest")
    $rest.addEventListener("click", function() {
        $rest.classList.remove('is-active')
        $navbarBurgers.forEach(function(el) {
          el.classList.toggle("is-active")
        })
    })

    document.getElementById("togglePastEvents").addEventListener("click", togglePastEvents)

  </script>
  </body>
</html>
"""
)

with open("index.html", "w") as f:
    f.write(template.render(events=events))
