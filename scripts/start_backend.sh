#!/bin/bash

# AI Intelligence System - Backend Startup Script

echo "🚀 Starting AI Intelligence System Backend..."

# Navigate to backend directory
cd "$(dirname "$0")/../backend" || exit

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt -q

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found, copying from .env.example..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your API keys!"
    exit 1
fi

# Initialize database
echo "🗄️  Initializing database..."
python -m app.db.init_db

# Start the server
echo "✅ Starting server on http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo ""
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
