# stop2.0
Digital stop button for your mobile phone.

[![Build Status](https://travis-ci.org/STOP2/stop2.0-backend.svg?branch=master)](https://travis-ci.org/STOP2/stop2.0-backend) [![Coverage Status](https://coveralls.io/repos/github/STOP2/stop2.0-backend/badge.svg?branch=DigitransitService)](https://coveralls.io/github/STOP2/stop2.0-backend?branch=DigitransitService)

https://ohtuprojekti.jamo.fi/topic_descriptions/147

### For front-end developers

To run the latest release version of this project locally using docker execute this command in terminal:
```
docker run -p 5000:5000 stoptwo/backend
```
This will open the application on port 5000 of your localhost. Use a flag `-d` to run the container in detached mode.


### For developers

Run project locally using docker compose:
```
docker-compose build
docker-compose up
```
