#!/usr/bin/env bash
set -o errexit  # stop the script if there is an error

echo "🚀 Installing dependencies..."
pip install -r requirements.txt

echo "📦 Running migrations..."
python manage.py migrate --noinput

echo "✅ Build script finished!"
