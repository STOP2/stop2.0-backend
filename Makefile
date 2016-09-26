SHELL=/bin/bash

requirements: pyvenv
	pip install -r requirements.txt

run: test
	python src/stop.py

pyvenv:
	source venv/bin/activate
	export PYTHONPATH=$(pwd)/src/

test:
	coverage run -m --branch --source=src --omit=src/tests/* unittest discover -s src/tests
	coverage report -m


