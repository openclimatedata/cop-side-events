index.html: eu.yaml german.yaml unfccc.yaml wwf.yaml ndc.yaml brasil.yaml uk.yaml render.py template.html venv
	./venv/bin/python render.py

database.js:
	wget -N http://ec.europa.eu/clima/events/0124/js/database.js

cache/eu-schedule-rooms.json: database.js
	mv database.js local-database.js
	sed -i 's/var opDayEvent/\/\/var opDayEvent/' local-database.js
	cat output.js >> local-database.js
	node local-database.js

eu.yaml: eu.py cache/eu-schedule-rooms.json venv
	./venv/bin/python $<

cache/ndc-calendar-w1.ics:
	wget "http://www.ndcpartnershipcop.org/events/week/2018-12-03/?tribe_event_display=week&tribe-bar-date=2018-12-03&ical=1&tribe_display=week" -O cache/ndc-calendar-w1.ics

cache/ndc-calendar-w2.ics:
	wget "http://www.ndcpartnershipcop.org/events/week/2018-12-10/?tribe_event_display=week&tribe-bar-date=2018-12-10&ical=1&tribe_display=week" -O cache/ndc-calendar-w2.ics

ndc.yaml: ndc.py cache/ndc-calendar-w1.ics cache/ndc-calendar-w2.ics venv
	./venv/bin/python $<

cache/brasil-week-1.html:
	wget http://espacobrasil.gov.br/en/week-1/ -O cache/brasil-week-1.html

cache/brasil-week-2.html:
	wget http://espacobrasil.gov.br/en/week-2/ -O cache/brasil-week-2.html

cache/uk.html:
	wget https://www.events.great.gov.uk/ehome/index.php?eventid=200184147 -O cache/uk.html

uk.yaml: uk.py cache/uk.html venv
	./venv/bin/python $<

brasil.yaml: brasil.py cache/brasil-week-1.html cache/brasil-week-2.html venv
	./venv/bin/python $<

cache/german.html:
	wget "https://www.bmu.de/en/german-climate-pavilion/events/" -O cache/german.html

german.yaml: german.py cache/german.html venv
	./venv/bin/python $<

cache/unfccc.html:
	wget "https://seors.unfccc.int/seors/reports/events_list.html?session_id=COP%2024" -O cache/unfccc.html

unfccc.yaml: unfccc.py cache/unfccc.html venv
	./venv/bin/python $<

cache/wwf.html:
	wget https://wwfcep.org/cop/ -O cache/wwf.html

wwf.yaml: wwf.py cache/wwf.html venv
	./venv/bin/python $<

venv: requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur requirements.txt
	touch venv

clean:
	rm -rf index.html *.yaml *.ics cache/*.html cache/*.yaml cache/*.ics

.PHONY: clean
