SHELL=/bin/bash

requirements: stamps/requirements-done

stamps/requirements-done: venv
	(. ./venv/bin/activate && pip install -r requirements.txt)
	mkdir -p stamps
	touch $@

run:
	python src/stop.py

venv:
	virtualenv -p python3 venv

test: stamps/requirements-done
	(. ./venv/bin/activate && \
	 PYTHONPATH=src/ coverage run -m --branch --source=src \
	  --omit=src/tests/* unittest discover -s src/tests && \
	coverage report -m)

