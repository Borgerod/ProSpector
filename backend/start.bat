@echo off
echo starting first program.
START /B /WAIT cmd /c "extraction_part_1.bat"
echo The first program is executed successfully.
START /B cmd /c "extraction_part_2.bat"
echo All the programs are executed successfully
cmd /k