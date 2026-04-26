@echo off
echo Starting ProNax AI Web Server...
echo.

REM Try to find Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python not found in PATH. Trying alternative paths...
    
    REM Try Microsoft Store Python
    C:\Users\%USERNAME%\AppData\Local\Microsoft\WindowsApps\python.exe --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo Python not found. Please install Python or add it to PATH.
        pause
        exit /b 1
    )
    
    set PYTHON_CMD=C:\Users\%USERNAME%\AppData\Local\Microsoft\WindowsApps\python.exe
) else (
    set PYTHON_CMD=python
)

echo Found Python: %PYTHON_CMD%
echo.

REM Start server
cd /d "%~dp0"
echo Starting server at http://localhost:8080
echo Press Ctrl+C to stop the server
echo.

%PYTHON_CMD% -m http.server 8080

pause
