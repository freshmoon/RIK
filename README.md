# Windows 系統監控器 (Windows System Monitor)

一個簡潔美觀的Windows桌面應用程式，顯示日曆和即時CPU使用率監控。

A clean and beautiful Windows desktop application that displays a calendar and real-time CPU usage monitoring.

## 功能特色 (Features)

- **左側日曆面板** - 顯示當月日曆，高亮今日日期
- **右側CPU監控** - 即時CPU使用率顯示，包含歷史圖表
- **中文界面** - 完全中文化的使用者介面
- **即時更新** - CPU使用率每秒更新
- **美觀設計** - 現代化的GUI設計

- **Left Calendar Panel** - Monthly calendar with today's date highlighted
- **Right CPU Monitor** - Real-time CPU usage with historical chart
- **Chinese Interface** - Fully localized Chinese user interface
- **Real-time Updates** - CPU usage updates every second
- **Beautiful Design** - Modern GUI design

## 系統需求 (System Requirements)

- Windows 7/8/10/11
- Python 3.7+ (僅建置時需要 / Only needed for building)

## 快速開始 (Quick Start)

### 方法1: 使用建置腳本 (Method 1: Using Build Script)

1. **下載專案檔案**
   Download project files:
   ```bash
   git clone https://github.com/freshmoon/RIK/Cursor.git
   cd Cursor
   ```
   或直接下載ZIP檔案 / Or download ZIP file directly

2. **執行建置腳本**
   Run the build script:
   ```
   雙擊 build.bat
   Double-click build.bat
   ```

3. **執行程式**
   Run the application:
   ```
   在 dist/ 資料夾中找到 SystemMonitor.exe
   Find SystemMonitor.exe in the dist/ folder
   ```

### 方法2: 手動建置 (Method 2: Manual Build)

1. **安裝Python相依套件**
   Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **建置可執行檔**
   Build executable:
   ```bash
   python build_windows_exe.py
   ```

3. **執行程式**
   Run the application:
   ```bash
   dist/SystemMonitor.exe
   ```

### 方法3: 直接執行Python程式 (Method 3: Direct Python Execution)

```bash
pip install -r requirements.txt
python windows_system_monitor.py
```

## 檔案說明 (File Description)

- `windows_system_monitor.py` - 主程式檔案
- `requirements.txt` - Python相依套件清單
- `build_windows_exe.py` - 建置腳本
- `build.bat` - Windows批次建置檔
- `README.md` - 說明文件

## 應用程式功能詳解 (Application Features)

### 日曆面板 (Calendar Panel)
- 顯示當前月份的完整日曆
- 今日日期以藍色背景高亮顯示
- 顯示年月日和星期
- 中文星期顯示（一至日）

### CPU監控面板 (CPU Monitoring Panel)
- 即時CPU使用率百分比顯示
- 進度條顯示當前使用率
- CPU核心數資訊
- 最近50秒的使用率歷史圖表
- 每秒自動更新數據

## 技術規格 (Technical Specifications)

- **GUI框架**: Tkinter (Python內建)
- **圖表**: Matplotlib
- **系統監控**: psutil
- **打包工具**: PyInstaller
- **更新頻率**: 1秒
- **歷史數據**: 50秒

## 疑難排解 (Troubleshooting)

### 建置問題 (Build Issues)

**問題**: `pyinstaller` 命令找不到
**解決**: 安裝PyInstaller
```bash
pip install pyinstaller
```

**問題**: 缺少模組錯誤
**解決**: 安裝所有相依套件
```bash
pip install -r requirements.txt
```

**問題**: 可執行檔無法運行
**解決**: 檢查Windows版本相容性，確保目標電腦有必要的運行庫

### 運行問題 (Runtime Issues)

**問題**: CPU使用率顯示為0%
**解決**: 等待幾秒讓系統收集數據

**問題**: 圖表不顯示
**解決**: 確保matplotlib正確安裝

## 自訂設定 (Customization)

您可以修改 `windows_system_monitor.py` 中的以下設定：

- 視窗大小：修改 `self.root.geometry("1000x600")`
- 更新頻率：修改 `self.root.after(1000, self.update_gui)` 中的1000（毫秒）
- 歷史數據量：修改 `deque(maxlen=50)` 中的50
- 顏色主題：修改各種 `bg` 和 `fg` 參數

## 授權 (License)

此專案採用MIT授權。
This project is licensed under the MIT License.

## 儲存庫 (Repository)

GitHub: https://github.com/freshmoon/RIK/Cursor

## 貢獻 (Contributing)

歡迎提交問題報告和功能請求！
Issues and feature requests are welcome!

如需回報問題或建議新功能，請前往：
For bug reports or feature requests, please visit:
https://github.com/freshmoon/RIK/Cursor/issues