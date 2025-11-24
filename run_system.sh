#!/bin/bash
cd "$(dirname "$0")"

# Kill any existing processes on ports 8000 and 5173
fuser -k 8000/tcp > /dev/null 2>&1
fuser -k 5173/tcp > /dev/null 2>&1

echo "🚀 Starting Sentinel AI System..."

# Start Backend
echo "Starting Backend API..."
uvicorn src.api:app --reload --port 8000 &
BACKEND_PID=$!

# Start Frontend
echo "Starting Frontend..."
cd frontend
npm run dev &
FRONTEND_PID=$!

echo "✅ System Online!"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:5173"

# Trap Ctrl+C to kill both processes
trap "kill $BACKEND_PID $FRONTEND_PID; exit" SIGINT

wait
