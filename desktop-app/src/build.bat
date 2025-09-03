@echo off

REM Usunięcie folderów i pliku
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist ControllerTester.spec del /q ControllerTester.spec

REM Uruchomienie PyInstaller
REM --windowed later
pyinstaller --contents-directory=. --noconfirm --onedir --add-data=C:\Users\damia\anaconda3\envs\PS5ControllerTester\Lib\site-packages\customtkinter:customtkinter --add-data=C:\Users\damia\anaconda3\envs\PS5ControllerTester\Lib\site-packages\dualsense_controller:dualsense_controller --add-data=hidapi.dll:. --add-data=assets:assets --name ControllerTester main.py

REM Przejście do folderu dist i spakowanie do ZIP
REM cd dist
REM powershell -command "Compress-Archive -Path ControllerTester.exe -DestinationPath ControllerTester.zip"

pause