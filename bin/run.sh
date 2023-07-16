#!/bin/sh
gunicorn --log-level debug -b 0.0.0.0:8080 --timeout=300 --worker-class=uvicorn.workers.UvicornWorker --workers 10 src.main:app
