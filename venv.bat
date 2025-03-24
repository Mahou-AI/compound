@echo off
if not exist ".venv" (
    echo create venv
    python -m venv .venv
) else (
    echo venv has been created.
) 
SET python=%~dp0.venv\Scripts\python.exe
SET source=https://pypi.org/simple
echo use "%python%"
echo source "%source%"
%python% -m ensurepip
%python% -m pip install --upgrade pip -i %source%
%python% -m pip install -r requirements.txt -i %source%
pause