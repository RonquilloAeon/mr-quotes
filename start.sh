#!/bin/bash

exec gunicorn -w 2 -k uvicorn.workers.UvicornWorker --log-level $LOG_LEVEL src.application.app:app -b 0.0.0.0 "$@"
