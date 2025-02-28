@echo off

REM Usunięcie folderów i pliku
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist ControllerTester.spec del /q ControllerTester.spec

REM Uruchomienie PyInstaller
pyinstaller --onefile --name ControllerTester main.py

REM Przejście do folderu dist i spakowanie do ZIP
cd dist
powershell -command "Compress-Archive -Path ControllerTester.exe -DestinationPath ControllerTester.zip"

pause