@echo off
start /min cmd /k "cd fast_api_server & uvicorn main:app --reload"
