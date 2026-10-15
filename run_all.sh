#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
echo "=== 01 turtle ==="; python3 experiments/01_turtle_geometry.py
echo "=== 02 verbosity ==="; python3 experiments/02_verbosity_benchmark.py
echo "=== 03 rubygems (live) ==="; python3 experiments/03_rubygems_live.py || true
echo "=== 04 github (live) ==="; python3 experiments/04_github_live.py || true
echo "=== 05 stackexchange (live) ==="; python3 experiments/05_stackexchange_live.py || true
echo "=== 06 pedagogy ==="; python3 experiments/06_pedagogy_matrix.py
echo "=== 07 hidden patterns ==="; python3 experiments/07_hidden_patterns.py
echo "=== 08 assets (GIF+charts) ==="; python3 experiments/08_make_assets.py
echo "ALL DONE — see results/ + data/"
ls -la results/ data/ || true
