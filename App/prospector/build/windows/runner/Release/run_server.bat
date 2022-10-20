@echo off
start /min cmd /k "cd api_server/server_backend/fast_api_server/backend & uvicorn main:app --reload"