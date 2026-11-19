@echo off
REM Opens a ready-to-use prompt (environment on, PostgreSQL on the path).
cd /d "%~dp0"
call .venv\Scripts\activate
set "PATH=C:\Program Files\PostgreSQL\18\bin;%PATH%"
cmd /k