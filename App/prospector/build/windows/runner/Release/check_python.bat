@ECHO off
:tryRun
@rem python python_test.py
if %ERRORLEVEL% neq 0 goto NoPython

::runServer
echo Python exist, running server...
echo run_server.bat
exit

::NoPython
echo Python does not exist, installing python...
python_installer.bat
pythonpath.bat
goto runServer
exit

