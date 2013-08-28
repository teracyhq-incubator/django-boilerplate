#!/bin/bash

#jenkins bash script build

pip install -r requirements/dev.txt

# style report
pep8 . > pep8_report.txt

pylint --rcfile .pylintrc -f parseable *.py settings urls apps libs > pylint_report.txt || exit 0

# coverage erase
# ./manage.py test
# coverage xml