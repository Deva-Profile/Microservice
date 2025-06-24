#!/bin/bash
set -e

echo "Applying database migrations..."
python manage.py migrate

echo "Starting server..."
gunicorn user_service.wsgi:application --bind 0.0.0.0:8000
