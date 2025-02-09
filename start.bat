@echo off

echo Setting up venv...
set VENV_DIR=".venv"
python -m venv %VENV_DIR%
call %VENV_DIR%\Scripts\activate

echo Installing requirements...
pythom -m pip install --upgrade pip
@REM pip install -r requirements.txt
python -m pip install -r requirements.txt
pip list
echo Migrating...
python manage.py migrate --settings=config.settings.local

echo Adding data to database...
echo from database import * | python manage.py shell