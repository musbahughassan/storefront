#!/bin/sh
set -e

host="${DATABASE_HOST:-db}"
port="${DATABASE_PORT:-5432}"

echo "Waiting for Postgres at $host:$port..."

until python -c "
import socket, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)
try:
    s.connect(('$host', $port))
except OSError:
    sys.exit(1)
"; do
  echo "Postgres is unavailable - sleeping"
  sleep 1
done

echo "Postgres is up."

exec "$@"
