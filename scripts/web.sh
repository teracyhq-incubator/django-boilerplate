#!/usr/bin/env bash

exec newrelic-admin run-program gunicorn project.wsgi --log-file -
