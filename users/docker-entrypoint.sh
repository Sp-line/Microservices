#!/bin/sh

set -e

echo "🚀 Starting User Service..."

echo "🔄 Running migrations..."
alembic upgrade head

echo "✅ Starting Server..."
exec "$@"