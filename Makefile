index.html: eu.yaml german.yaml unfccc.yaml wwf.yaml ndc.yaml render.py venv
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
	rm -rf index.html *.yaml *.ics

.PHONY: clean
