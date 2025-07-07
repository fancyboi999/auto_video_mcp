#!/bin/sh
set -e

# 执行数据库迁移
echo "Running database migrations..."
alembic upgrade head

# 启动服务器
echo "Starting auto_video_mcp server..."
exec python -m auto_video_mcp.server --transport http --host 0.0.0.0 --port 8000 