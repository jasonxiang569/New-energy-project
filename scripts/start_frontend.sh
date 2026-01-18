#!/bin/bash

# AI Intelligence System - Frontend Startup Script

echo "🚀 Starting AI Intelligence System Frontend..."

# Navigate to frontend directory
cd "$(dirname "$0")/../frontend" || exit

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing dependencies..."
    npm install
fi

# Start the development server
echo "✅ Starting development server on http://localhost:5173"
echo ""
npm run dev
