index.html: eu.yaml german.yaml unfccc.yaml wwf.yaml render.py venv
	./venv/bin/python render.py

database.js:
	wget -N http://ec.europa.eu/clima/events/0124/js/database.js

schedule-rooms.json: database.js
	mv database.js local-database.js
	sed -i 's/var opDayEvent/\/\/var opDayEvent/' local-database.js
	cat output.js >> local-database.js
	node local-database.js

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
	rm -rf index.html *.yaml

.PHONY: clean
