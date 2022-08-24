@echo off
echo starting first program.
START /B /WAIT cmd /c "test1.bat"
echo The first program is executed successfully.
START /B cmd /c "extraction.bat"
echo All the programs are executed successfully
cmd /k