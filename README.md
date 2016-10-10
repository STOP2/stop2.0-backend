# stop2.0
Digital stop button for your mobile phone.

[![Build Status](https://travis-ci.org/STOP2/stop2.0-backend.svg?branch=master)](https://travis-ci.org/STOP2/stop2.0-backend) [![Coverage Status](https://coveralls.io/repos/github/STOP2/stop2.0-backend/badge.svg?branch=DigitransitService)](https://coveralls.io/github/STOP2/stop2.0-backend?branch=DigitransitService)

https://ohtuprojekti.jamo.fi/topic_descriptions/147

## For front-end developers

To run the latest release version of this project locally using Docker execute this command in terminal:
```   
docker run -p 5000:5000 stoptwo/backend
```
This will open the application on port 5000 of your localhost. Use a flag -d to run the container in detached mode.

To kill all docker images running on background:
```    
docker stop $(docker ps -q)
```

## For developers

### Setting up a Development Environment for Linux

Python version: 3.5.2

Recommended IDE: [PyCharm Professional](https://www.jetbrains.com/pycharm/). Students can apply for a free student license [here](https://www.jetbrains.com/student/).

To avoid any conflicting dependencies with your other projects, install virtualenv with one of these three installation commands:
```
sudo easy_install virtualenv
```
or
```
sudo pip install virtualenv
```
or
```
sudo apt-get install python-virtualenv
```

in your project folder (../stop2.0-backend)
```
virtualenv venv
. venv/bin/activate
```
Now you are in the virtualenv environment. To go back to the normal environment:
```
deactivate
```

In your virtualenv install Flask:
```
pip install Flask
```

For more information about installing Flask: http://flask.pocoo.org/docs/0.11/installation/

To install all requirements needed for this project:
```
pip install -r requirements.txt
```

(if installing psycopg2 fails, you may need to install following dependencies to your system in normal environment:
    sudo apt-get install libpq-dev python-dev
)

To prevent import problems for modules, in your project’s root folder:
```    
export PYTHONPATH=$(pwd)/src/
```

### Running project locally on a Docker container

For instructions installing Docker Engine on Linux please see: https://docs.docker.com/engine/installation/linux/

Build a dockerfile and run it locally:
```
docker build -t stop .
docker run -p 5000:5000 stop
```
You can add flag `-d`to your `docker run` command to run the container in detached mode.

Stop the container by executing `docker ps` to find the container id and then executing `docker stop {container id}`.

Run project’s database locally using Docker:
```
docker build -f DB-Dockerfile -t db .
docker run -p 5432:5432 db
```

Docker Compose is a tool for defining and running multi-container Docker apps. To run project locally using Docker Compose:
```
docker-compose build
docker-compose up
```
