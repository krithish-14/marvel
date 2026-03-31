#!/bin/bash
pip install -r requirements.txt
python manage.py collectstatic --noinput

# Run DB Migrations (for SQLite fallback on Vercel)
python manage.py migrate

# Prepopulate database records for Vercel artifact
python populate_characters.py
python populate_comics.py
