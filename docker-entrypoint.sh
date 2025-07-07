#!/bin/bash
set -e

# Decode the base64 config and write it to a file
if [ -n "$CONFIG_JSON_BASE64" ]; then
  echo "$CONFIG_JSON_BASE64" | base64 -d > /app/config.json
fi

# Execute the main process
exec python -m auto_video_mcp.server