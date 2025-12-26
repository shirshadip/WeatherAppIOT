@echo off
echo ================================
echo Python Environment Setup Script
echo ================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python first.
    pause
    exit /b
)

echo ✅ Python detected

REM Create virtual environment
if not exist venv (
    echo 📦 Creating virtual environment...
    python -m venv venv
) else (
    echo ⚠️ Virtual environment already exists
)

REM Activate virtual environment
echo 🔌 Activating virtual environment...
call venv\Scripts\activate

REM Upgrade pip
echo ⬆️ Upgrading pip...
python -m pip install --upgrade pip

REM Install required packages
echo 📥 Installing required packages...
pip install pyserial flask

echo ================================
echo ✅ Setup completed successfully
echo ================================
echo To activate later, run:
echo venv\Scripts\activate
pause
