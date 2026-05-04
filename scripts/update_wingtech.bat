@echo off
chcp 65001 >nul
cd /d C:\Users\hozen\.openclaw\workspace\li-lu-research
python.exe -X utf8 scripts\update_wingtech.py
