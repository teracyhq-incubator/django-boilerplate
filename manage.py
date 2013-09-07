#!/usr/bin/env python
"""
A thin wrapper around django-admin.py that takes care of two things for you before delegating to
django-admin.py
It puts your project package on sys.path.
It sets the DJANGO_SETTINGS_MODULE environment variable so that it points to your project
settings.py file.
"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.project.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
