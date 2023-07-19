#!/bin/sh
gunicorn --log-level debug -b 0.0.0.0:80 --timeout=100 --worker-class=uvicorn.workers.UvicornWorker --workers 1 appfoo.views:app
