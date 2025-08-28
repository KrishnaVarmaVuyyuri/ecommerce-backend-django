#!/usr/bin/env bash
set -o errexit  # stop the script if there is an error

echo "🚀 Installing dependencies..."
pip install -r requirements.txt

echo "📦 Running migrations..."
python manage.py migrate --noinput

echo "✅ Build script finished!"

echo "👤 Creating superuser..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username="varma").exists():
    User.objects.create_superuser("varma", "varma.vuyyuri01@gmail.com", "12345")
EOF

