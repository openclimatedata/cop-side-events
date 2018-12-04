index.html: eu.yaml german.yaml unfccc.yaml wwf.yaml ndc.yaml brasil.yaml uk.yaml render.py template.html venv
	./venv/bin/python render.py

database.js:
	wget -N http://ec.europa.eu/clima/events/0124/js/database.js

schedule-rooms.json: database.js
	mv database.js local-database.js
	sed -i 's/var opDayEvent/\/\/var opDayEvent/' local-database.js
	cat output.js >> local-database.js
	node local-database.js

ndc-calendar-w1.ics:
	wget "http://www.ndcpartnershipcop.org/events/week/2018-12-03/?tribe_event_display=week&tribe-bar-date=2018-12-03&ical=1&tribe_display=week" -O ndc-calendar-w1.ics

ndc-calendar-w2.ics:
	wget "http://www.ndcpartnershipcop.org/events/week/2018-12-10/?tribe_event_display=week&tribe-bar-date=2018-12-10&ical=1&tribe_display=week" -O ndc-calendar-w2.ics

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

ndc.yaml: ndc.py ndc-calendar-w1.ics ndc-calendar-w2.ics venv
	./venv/bin/python $<

eu.yaml: eu.py schedule-rooms.json venv
	./venv/bin/python $<

german.yaml: german.py venv
	./venv/bin/python $<

unfccc.yaml: unfccc.py venv
	./venv/bin/python $<

wwf.yaml: wwf.py venv
	./venv/bin/python $<

venv: requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur requirements.txt
	touch venv

clean:
	rm -rf index.html *.yaml *.ics cache/*.html cache/*.yaml cache/*.ics

.PHONY: clean
