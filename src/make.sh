#!/bin/sh
# full rebuild: v1 slides -> v2 design pass -> v3 media chapter -> index.html
cd "$(dirname "$0")/.." && python3 src/v2.py && python3 src/v4.py && python3 src/v5.py && python3 src/v6.py && python3 src/v7.py && python3 src/build.py
