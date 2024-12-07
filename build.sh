#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "Checking required environment variables..."
: "${DATABASE_URL:?DATABASE_URL is not set}"
: "${SECRET_KEY:?SECRET_KEY is not set}"

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Applying database migrations..."
python manage.py migrate

echo "Build script completed successfully."
