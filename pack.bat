@echo off
if not exist ".venv" (
    call "./venv.bat"
)
SET python=%~dp0.venv\Scripts\python.exe

%python% "./src/pack/main.py"