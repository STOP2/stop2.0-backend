run: pyvenv requirements test
	python stop.py

requirements:
	pip install requirements.txt

pyvenv:
	cd ..
	source venv/bin/activate
	export PYTHONPATH=$(pwd)/src/

test:
	coverage run -m --branch --source=src --omit=src/tests/* unittest discover -s src/tests
	coverage report -m