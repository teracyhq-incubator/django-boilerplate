#!/usr/bin/env bash

exec gunicorn project.wsgi
