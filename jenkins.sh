#!/bin/bash

#jenkins bash script build

pip install -r requirements/dev.txt

# style report
flake8 --max-complexity 12 .

pep8 . > pep8_report.txt

coverage erase
# unit test report
coverage run --branch --source=apps,libs manage.py test --with-xunit

# coverage report
coverage xml

# must be the last command to exit 0, otherwise, the next command will not be executed.
pylint --rcfile .pylintrc -f parseable *.py settings urls apps libs > pylint_report.txt || exit 0
