#!/usr/bin/env bash

if [ -z $HOST ]; then
    HOST="0.0.0.0"
fi

if [ -z $PORT ]; then
    PORT=5000
fi

gunicorn -w 3 -b $HOST:$PORT stop:app
