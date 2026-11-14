#!/bin/bash
# Double-click: search Hugging Face, HDX and Google Earth Engine for candidate datasets
# and write data/candidate_datasets.csv. Takes a few minutes.
cd "$(dirname "$0")" && python3 scripts/harvest_datasets.py; echo; echo "Done. You can close this window."
