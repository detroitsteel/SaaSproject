#!/bin/sh
if ! test -f "randomized_chart_data.sqlite"; then unzip randomized_chart_data.zip; fi
export FLASK_APP=./chartdata/index.py
#source $(pipenv --venv)/bin/activate
flask run -h 0.0.0.0
