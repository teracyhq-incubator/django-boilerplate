#!/usr/bin/env bash

exec celery -A project worker -B -l info
