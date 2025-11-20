# Manim Animation - Best Time to Buy and Sell Stock II

This repository contains a Manim Community animation that visually explains the LeetCode problem "Best Time to Buy and Sell Stock II".

## What's included
- `animation.py` — Main Manim scene (StockProfitScene)
- `requirements.txt` — Minimal requirements
- `README.md` — This file

## Requirements
- Python 3.9+
- Manim Community Edition

## Install (recommended)
```bash
python -m venv venv
# macOS / Linux
source venv/bin/activate
# Windows PowerShell
venv\Scripts\activate

pip install -U pip
pip install -r requirements.txt

manim -pql animation.py StockProfitScene

manim -p -r 1920,1080 animation.py StockProfitScene




---

### 3) `requirements.txt`



---

### 4) Optional helper: `zipme.sh` (Linux / macOS)
```bash
#!/usr/bin/env bash
set -e
OUT=manim-stock-problem-community.zip
rm -f "$OUT"
zip -r "$OUT" animation.py README.md requirements.txt
echo "Created $OUT"
