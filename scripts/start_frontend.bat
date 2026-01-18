@echo off
REM AI Intelligence System - Frontend Startup Script (Windows)

echo Starting AI Intelligence System Frontend...

cd /d "%~dp0..\frontend"

REM Check if node_modules exists
if not exist "node_modules\" (
    echo Installing dependencies...
    call npm install
)

REM Start the development server
echo Starting development server on http://localhost:5173
echo.
call npm run dev
