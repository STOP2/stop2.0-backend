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
	(docker-compose build && docker-compose up -d && . ./venv/bin/activate && \
	 PYTHONPATH=src/ coverage run -m --branch --source=src \
	  --omit=src/tests/* unittest discover -s src/tests && \
	coverage report -m && . src/tests/integration_test.sh) && \
	docker stop stop20backend_web_1 && \
    docker stop stop20backend_postgres_1

