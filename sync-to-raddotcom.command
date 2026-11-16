#!/bin/bash
# Double-click: rebuild build/problems.json and copy it into the raddotcom site,
# so rheamad.vercel.app/ai-problems shows the current database.
# raddotcom lives at ~/code/raddotcom; set RADDOTCOM to point elsewhere.
RAD="${RADDOTCOM:-$HOME/code/raddotcom}"
cd "$(dirname "$0")" || exit 1
if [ ! -d "$RAD/static" ]; then echo "Can't find raddotcom at $RAD"; exit 1; fi
if python3 scripts/validate.py && python3 scripts/export_json.py \
   && python3 scripts/sync_merge.py build/problems.json "$RAD/static/ai-problems.json"; then
  echo "Copied to $RAD/static/ai-problems.json. Commit and push raddotcom to deploy."
else
  echo "Stopped: fix the errors above first."; exit 1
fi
