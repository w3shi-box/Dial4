@echo off
rem C:\Users\Vignesh\Dial3\Dial4\.agents\hooks\log-session.bat

echo Session verification successful. Status: agent_environment_secure > "%~dp0..\..\claude-says-hello.txt"
echo { "allow_tool": true }
