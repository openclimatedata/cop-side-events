import yaml
from jinja2 import Environment

env = Environment(extensions=["jinja2_time.TimeExtension"])

sources = ["german.yaml", "unfccc.yaml", "wwf.yaml"]

events = []

for source in sources:
    data = yaml.load(open(source, "r"))
    events += data

events = sorted(events, key=lambda k: (k["start"], k["location"]))

template = env.from_string(
    """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>COP24 Side Events</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.2/css/bulma.min.css">
    <style>
      .container {
        max-width: 768px;
      }
      .section {
        padding: 0 1rem 0 1rem;
      }
    </style>
  </head>
  <body class="has-navbar-fixed-top">
  <nav class="navbar is-fixed-top is-dark" role="navigation" aria-label="main navigation dropdown">
  <div class="navbar-brand">
    <a class="navbar-item" href="#">
      #COP24&nbsp;<span class="is-hidden-mobile"> (Unofficial) Side Event Aggregator</span>
    </a>
    <a class="navbar-item" id="next" href="#next">Next</a>

    <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbar-rest">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div class="navbar-menu" id="navbar-rest">
    <div class="navbar-start">
      <span class="navbar-item is-hidden-mobile">December</span>
      <a class="navbar-item" id="dec02" href="#02">02</a>
      <a class="navbar-item" id="dec03" href="#03">03</a>
      <a class="navbar-item" id="dec04" href="#04">04</a>
      <a class="navbar-item" id="dec05" href="#05">05</a>
      <a class="navbar-item" id="dec06" href="#06">06</a>
      <a class="navbar-item" id="dec07" href="#07">07</a>
      <a class="navbar-item" id="dec08" href="#08">08</a>
      <a class="navbar-item" id="dec09" href="#09">09</a>
      <a class="navbar-item" id="dec10" href="#10">10</a>
      <a class="navbar-item" id="dec11" href="#11">11</a>
      <a class="navbar-item" id="dec12" href="#12">12</a>
      <a class="navbar-item" id="dec13" href="#13">13</a>
      <a class="navbar-item" id="dec14" href="#14">14</a>
    </div>
    <div class="navbar-end">
      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">Sources</a>
        <div class="navbar-dropdown">
          <a href="https://seors.unfccc.int/seors/reports/events_list.html?session_id=COP%2024" class="navbar-item">UNFCCC Side Events</a>
          <a href="https://www.bmu.de/en/german-climate-pavilion/events/" class="navbar-item">German Pavilion</a>
          <a href="https://wwf.panda.org/our_work/climate_and_energy/cop24/" class="navbar-item">WWF Pavilion</a>
        </div>
      </div>
      <a href="https://twitter.com/openclimatedata" class="navbar-item">Made by  @openclimatedata</a>
    </div>
  </div>
  </nav>
  <div class="container">
    <section class="section">
    Last Update: {% now 'Europe/Berlin', '%a, %d %b %Y %H:%M' %}
    </section>
    {% for event in events %}
      <section class="section is-size-5 is-size-6-mobile">
      <p class="is-size-4 is-size-5-mobile">{{ event.day.strftime('%A, %d %B') }}<br>
      <time datetime="{{ event.start.strftime("%Y-%m-%d %H:%M") }}">{{ event.start.strftime("%H:%M") }}</time> -
      {% if event.end %}
        {{ event.end.strftime("%H:%M") }}
      {% endif %}
      </p>
      <h2 class="is-size-3 is-size-4-mobile"><a class="has-text-primary" href="{{ event.source }}">{{ event.location }}</a><br> {{ event.title }}</h2>
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
      </section>
      <hr>
    {% endfor %}
  </div>
  <script>
    var now = new Date()
    var times = document.getElementsByTagName("time")
    var timestamps = []
    for (var i = 0; i < times.length; i++) {
        timestamps.push(new Date(times[i].attributes["datetime"].value))
    }

    var toDay = function(day) {
        for (var i = 0; i < timestamps.length; i++) {
            if (timestamps[i].getDate() >= day) {
              times[i].scrollIntoView()
              window.scrollBy(0, -120)
              break
            }
        }
    }

    var next = function() {
        for (var i = 0; i < timestamps.length; i++) {
            if (timestamps[i] >= now) {
              times[i].scrollIntoView()
              window.scrollBy(0, -120)
              break
            }
        }
    }
    next()
    document.getElementById("next").addEventListener('click', next)
    document.getElementById("dec02").addEventListener('click', function() {toDay(2)})
    document.getElementById("dec03").addEventListener('click', function() {toDay(3)})
    document.getElementById("dec04").addEventListener('click', function() {toDay(4)})
    document.getElementById("dec05").addEventListener('click', function() {toDay(5)})
    document.getElementById("dec06").addEventListener('click', function() {toDay(6)})
    document.getElementById("dec07").addEventListener('click', function() {toDay(7)})
    document.getElementById("dec08").addEventListener('click', function() {toDay(8)})
    document.getElementById("dec09").addEventListener('click', function() {toDay(9)})
    document.getElementById("dec10").addEventListener('click', function() {toDay(10)})
    document.getElementById("dec11").addEventListener('click', function() {toDay(11)})
    document.getElementById("dec12").addEventListener('click', function() {toDay(12)})
    document.getElementById("dec13").addEventListener('click', function() {toDay(13)})
    document.getElementById("dec14").addEventListener('click', function() {toDay(14)})


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



  </script>
  </body>
</html>
"""
)

with open("index.html", "w") as f:
    f.write(template.render(events=events))
