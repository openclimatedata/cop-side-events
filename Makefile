index.html: german.yaml unfccc.yaml wwf.yaml render.py venv
	./venv/bin/python render.py

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
