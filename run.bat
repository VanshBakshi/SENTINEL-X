@echo off
title SENTINEL-X AI Threat Intelligence
echo.
echo ============================================
echo       SENTINEL-X SOC PLATFORM
echo ============================================
if not exist .venv python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt
echo.
echo Running demo investigation...
python main.py --input data/demo
echo.
echo Starting dashboard...
streamlit run app.py
