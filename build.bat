@echo off
echo ==========================================
echo Windows System Monitor Build Script
echo 正在建置Windows系統監控器
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1 || python3 --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo 錯誤: Python未安裝或不在系統路徑中
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Python detected, starting build process...
echo 偵測到Python，開始建置程序...
echo.

REM Run the Python build script (try python first, then python3)
python build_windows_exe.py 2>nul || python3 build_windows_exe.py

echo.
echo Build process completed!
echo 建置程序完成！
echo.

REM Check if executable was created
if exist "dist\SystemMonitor.exe" (
    echo SUCCESS: SystemMonitor.exe created successfully!
    echo 成功: SystemMonitor.exe 建置成功！
    echo Location: dist\SystemMonitor.exe
    echo 位置: dist\SystemMonitor.exe
) else (
    echo WARNING: Executable not found in dist folder
    echo 警告: 在dist資料夾中找不到可執行檔
)

echo.
echo Press any key to exit...
echo 按任意鍵結束...
pause >nul