@echo off
setlocal
cd /d "%~dp0"
echo [OpenStudy] Checking Python...
if not exist ".venv\Scripts\python.exe" (
    py -m venv .venv
    if errorlevel 1 (
        echo Could not create Python virtual environment.
        pause
        exit /b 1
    )
)
echo [OpenStudy] Installing requirements...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failed
echo [OpenStudy] Applying migrations...
".venv\Scripts\python.exe" manage.py migrate
if errorlevel 1 goto failed
echo [OpenStudy] Adding demo courses...
".venv\Scripts\python.exe" manage.py seed_demo
if errorlevel 1 goto failed
echo Open http://127.0.0.1:8000/ in a browser.
".venv\Scripts\python.exe" manage.py runserver
goto done
:failed
echo Setup failed. See the error above.
pause
:done
endlocal
