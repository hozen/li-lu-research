@echo off
chcp 65001 >nul
cd /d C:\Users\hozen\.openclaw\workspace\li-lu-research
python scripts\extract_key_moments.py transcripts\li-lu-byd-2026-full.srt
