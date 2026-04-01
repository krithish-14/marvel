#!/bin/bash
set -e
echo 'Starting Build...'
python3 -m pip install -r requirements.txt --break-system-packages
echo 'Collecting Static Files...'
python3 manage.py collectstatic --noinput
echo 'Running Migrations...'
python3 manage.py migrate
echo 'Build Completed.'
