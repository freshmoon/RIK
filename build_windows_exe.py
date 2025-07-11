#!/usr/bin/env python3
"""
Build script to create Windows executable for the System Monitor application.
This script uses PyInstaller to package the Python application into a standalone .exe file.

GitHub Repository: https://github.com/freshmoon/RIK/Cursor
"""

import os
import subprocess
import sys

def build_executable():
    """Build Windows executable using PyInstaller."""
    
    print("正在建置Windows可執行檔...")
    print("Building Windows executable...")
    
    # PyInstaller command to create executable
    cmd = [
        'pyinstaller',
        '--onefile',                    # Create single executable file
        '--windowed',                   # Hide console window
        '--name=SystemMonitor',         # Name of the executable
        '--icon=icon.ico',              # Icon file (if available)
        '--add-data=requirements.txt;.', # Include requirements file
        'windows_system_monitor.py'     # Main Python file
    ]
    
    # Remove icon parameter if icon file doesn't exist
    if not os.path.exists('icon.ico'):
        cmd.remove('--icon=icon.ico')
        print("注意: 沒有找到icon.ico檔案，將使用預設圖示")
        print("Note: icon.ico not found, using default icon")
    
    try:
        # Run PyInstaller
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("建置成功！")
        print("Build successful!")
        print(f"可執行檔位置: dist/SystemMonitor.exe")
        print(f"Executable location: dist/SystemMonitor.exe")
        
    except subprocess.CalledProcessError as e:
        print(f"建置失敗: {e}")
        print(f"Build failed: {e}")
        print(f"錯誤輸出: {e.stderr}")
        print(f"Error output: {e.stderr}")
        return False
    
    except FileNotFoundError:
        print("錯誤: 找不到PyInstaller。請先安裝：pip install pyinstaller")
        print("Error: PyInstaller not found. Please install: pip install pyinstaller")
        return False
    
    return True

def install_dependencies():
    """Install required dependencies."""
    print("正在安裝相依套件...")
    print("Installing dependencies...")
    
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--break-system-packages', '-r', 'requirements.txt'], 
                      check=True)
        print("相依套件安裝完成")
        print("Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("相依套件安裝失敗")
        print("Failed to install dependencies")
        return False

def main():
    """Main build process."""
    print("=== Windows系統監控器建置程序 ===")
    print("=== Windows System Monitor Build Process ===")
    print()
    
    # Check if Python file exists
    if not os.path.exists('windows_system_monitor.py'):
        print("錯誤: 找不到windows_system_monitor.py檔案")
        print("Error: windows_system_monitor.py file not found")
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    print()
    
    # Build executable
    if build_executable():
        print()
        print("=== 建置完成 ===")
        print("=== Build Complete ===")
        print("您可以在 dist/ 資料夾中找到 SystemMonitor.exe")
        print("You can find SystemMonitor.exe in the dist/ folder")
        print()
        print("使用說明:")
        print("Usage instructions:")
        print("1. 將 SystemMonitor.exe 複製到任何Windows電腦")
        print("1. Copy SystemMonitor.exe to any Windows computer")
        print("2. 雙擊執行即可使用")
        print("2. Double-click to run the application")
    else:
        print("建置失敗，請檢查錯誤訊息")
        print("Build failed, please check error messages")

if __name__ == "__main__":
    main()