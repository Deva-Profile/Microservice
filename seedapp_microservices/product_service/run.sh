#!/bin/bash
set -e  # Exit on any error

echo "🚀 Applying database migrations..."
python manage.py migrate --noinput

# Uncomment this if you're serving static files with WhiteNoise or similar
# echo "📦 Collecting static files..."
# python manage.py collectstatic --noinput

echo "🔥 Starting Gunicorn server..."
exec gunicorn product_project.wsgi:application --bind 0.0.0.0:8000
