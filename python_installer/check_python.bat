@ECHO off
:tryRun
@rem python python_test.py
if %ERRORLEVEL% neq 0 goto NoPython

::runServer
echo Python exist, continue...

rem --Refresh Environmental Variables
call RefreshEnv.cmd

rem --Use python, pip
python -m venv env
pip install -r fast_api_server\requirements.txt
exit

::NoPython
echo Python does not exist, installing python...
python_installer.bat
pythonpath.bat
exit