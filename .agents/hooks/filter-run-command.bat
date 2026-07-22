@echo off
rem C:\Users\Vignesh\Dial3\.agents\hooks\filter-run-command.bat

python -c "import sys, json; data = json.load(sys.stdin); cmd = data.get('toolCall', {}).get('args', {}).get('CommandLine', ''); is_blocked = any(x in cmd.lower() for x in ['rmdir /s', 'del /f', 'format', 'curl', 'wget']); print(json.dumps({'allow_tool': False, 'deny_reason': 'Security Policy: Restricted utility command block triggered on Windows.'} if is_blocked else {'allow_tool': True}))"
