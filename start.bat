@echo off
REM Starts the KurtonBerg development server.
cd /d "%~dp0"
call .venv\Scripts\activate
set "PATH=C:\Program Files\PostgreSQL\18\bin;%PATH%"
python manage.py check
python manage.py runserver
pause