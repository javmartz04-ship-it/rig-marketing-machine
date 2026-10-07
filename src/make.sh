#!/bin/sh
# full rebuild: v1 slides -> v2 design pass -> v3 media chapter -> index.html
cd "$(dirname "$0")/.." && python3 src/v2.py && python3 src/v3.py && python3 src/build.py
