#!/usr/bin/env bash
# Exit on error
set -o errexit

echo "Checking required environment variables..."
: "${DATABASE_URL:?DATABASE_URL is not set}"
: "${SECRET_KEY:?SECRET_KEY is not set}"

echo "Ensuring correct Python version..."
if ! python --version | grep -q "3.12"; then
    echo "Python 3.12 is required. Aborting."
    exit 1
fi

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Applying database migrations..."
python manage.py migrate

echo "Build script completed successfully."
