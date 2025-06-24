#!/bin/bash

# Apply migrations
python manage.py migrate --noinput

# Collect static files (if needed)
# python manage.py collectstatic --noinput

# Start Gunicorn server
gunicorn product_project.wsgi:application --bind 0.0.0.0:8000

