#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🔧 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📁 Creating static directory..."
mkdir -p static

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input

# Wait for database to be ready
echo "🔄 Waiting for database..."
sleep 10

echo "🗄️ Running database migrations..."
python manage.py migrate

echo "✅ Build completed successfully!"