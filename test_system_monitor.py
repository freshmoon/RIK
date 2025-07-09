#!/usr/bin/env python3
"""
Test script for system monitor functionality
Tests the core components without GUI to verify everything works.
"""

import calendar
import datetime
import psutil
import time
import sys

def test_calendar_functionality():
    """Test calendar display functionality."""
    print("=== 測試日曆功能 (Testing Calendar Functionality) ===")
    
    today = datetime.date.today()
    print(f"今日日期 (Today's Date): {today.strftime('%Y年%m月%d日 (%A)')}")
    
    # Get calendar data
    cal = calendar.monthcalendar(today.year, today.month)
    
    # Display calendar header
    print(f"\n{today.year}年{today.month}月")
    print("一  二  三  四  五  六  日")
    print("-" * 21)
    
    # Display calendar
    for week in cal:
        week_str = ""
        for day in week:
            if day == 0:
                week_str += "   "
            elif day == today.day:
                week_str += f"[{day:2d}]"  # Highlight today
            else:
                week_str += f" {day:2d} "
        print(week_str)
    
    print("✓ 日曆功能測試通過 (Calendar functionality test passed)")
    return True

def test_cpu_monitoring():
    """Test CPU monitoring functionality."""
    print("\n=== 測試CPU監控功能 (Testing CPU Monitoring) ===")
    
    try:
        # Get CPU info
        cpu_count = psutil.cpu_count()
        print(f"CPU 核心數 (CPU Cores): {cpu_count}")
        
        # Get CPU usage
        print("正在監控CPU使用率 (Monitoring CPU usage)...")
        for i in range(5):
            cpu_percent = psutil.cpu_percent(interval=1)
            print(f"CPU 使用率 (CPU Usage) #{i+1}: {cpu_percent:.1f}%")
        
        # Test CPU per core
        cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)
        print(f"各核心使用率 (Per-core usage): {[f'{c:.1f}%' for c in cpu_per_core]}")
        
        print("✓ CPU監控功能測試通過 (CPU monitoring test passed)")
        return True
        
    except Exception as e:
        print(f"✗ CPU監控測試失敗 (CPU monitoring test failed): {e}")
        return False

def test_imports():
    """Test all required imports."""
    print("\n=== 測試模組導入 (Testing Module Imports) ===")
    
    modules_to_test = [
        ('tkinter', 'tkinter'),
        ('matplotlib', 'matplotlib'),
        ('psutil', 'psutil'),
        ('calendar', 'calendar'),
        ('datetime', 'datetime'),
        ('threading', 'threading'),
        ('collections', 'collections'),
    ]
    
    failed_imports = []
    
    for module_name, import_name in modules_to_test:
        try:
            __import__(import_name)
            print(f"✓ {module_name} 導入成功 (imported successfully)")
        except ImportError as e:
            print(f"✗ {module_name} 導入失敗 (import failed): {e}")
            failed_imports.append(module_name)
    
    if failed_imports:
        print(f"\n缺少模組 (Missing modules): {', '.join(failed_imports)}")
        return False
    else:
        print("✓ 所有模組導入測試通過 (All module imports passed)")
        return True

def test_matplotlib_backend():
    """Test matplotlib backend configuration."""
    print("\n=== 測試Matplotlib後端 (Testing Matplotlib Backend) ===")
    
    try:
        import matplotlib
        # Set backend to Agg for headless operation
        matplotlib.use('Agg')
        
        import matplotlib.pyplot as plt
        from matplotlib.figure import Figure
        
        # Create a simple test plot
        fig = Figure(figsize=(6, 3), dpi=100)
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
        ax.set_title('測試圖表 (Test Chart)')
        
        print(f"Matplotlib 後端 (Backend): {matplotlib.get_backend()}")
        print("✓ Matplotlib測試通過 (Matplotlib test passed)")
        return True
        
    except Exception as e:
        print(f"✗ Matplotlib測試失敗 (Matplotlib test failed): {e}")
        return False

def main():
    """Main test function."""
    print("Windows 系統監控器 - 功能測試")
    print("Windows System Monitor - Functionality Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_matplotlib_backend,
        test_calendar_functionality,
        test_cpu_monitoring,
    ]
    
    passed_tests = 0
    total_tests = len(tests)
    
    for test in tests:
        try:
            if test():
                passed_tests += 1
        except Exception as e:
            print(f"✗ 測試失敗 (Test failed): {e}")
    
    print("\n" + "=" * 50)
    print(f"測試結果 (Test Results): {passed_tests}/{total_tests} 通過 (passed)")
    
    if passed_tests == total_tests:
        print("🎉 所有測試通過！可以建置Windows程式 (All tests passed! Ready to build Windows application)")
        print("\n建議下一步 (Next steps):")
        print("1. 執行 python3 build_windows_exe.py (Run build script)")
        print("2. 或雙擊 build.bat (Windows) (Or double-click build.bat on Windows)")
        return True
    else:
        print("❌ 部分測試失敗，請檢查相依套件 (Some tests failed, please check dependencies)")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)