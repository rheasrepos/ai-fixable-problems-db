#!/bin/bash
# Double-click: rebuild build/problems.json and copy it into the raddotcom site,
# so rheamad.vercel.app/ai-problems shows the current database.
cd "$(dirname "$0")" && python3 scripts/validate.py && python3 scripts/export_json.py \
  && cp build/problems.json ../raddotcom/static/ai-problems.json \
  && echo "Copied to raddotcom/static/ai-problems.json. Commit and push raddotcom to deploy." \
  || echo "Stopped: fix the errors above first."
