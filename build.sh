#!/usr/bin/env bash
# Install deps without relying on requirements.txt encoding (Windows UTF-16 breaks pip on Linux).
set -o errexit
pip install "Django==6.0.3" "whitenoise==6.12.0" "gunicorn==23.0.0"
python manage.py collectstatic --no-input
python manage.py migrate --noinput
