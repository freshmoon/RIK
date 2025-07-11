#!/usr/bin/env python3
"""
Windows System Monitor - 系統監控器
A desktop application displaying calendar and real-time CPU usage monitoring.

Features:
- Left panel: Monthly calendar with today's date highlighted
- Right panel: Real-time CPU usage monitoring with historical chart
- Chinese interface with modern GUI design

GitHub Repository: https://github.com/freshmoon/RIK/Cursor
"""

import tkinter as tk
from tkinter import ttk
import calendar
import datetime
import psutil
import threading
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from collections import deque

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("系統監控器 - 日曆與CPU使用率")
        self.root.geometry("1000x600")
        self.root.configure(bg='#f0f0f0')
        
        # CPU data for graph
        self.cpu_data = deque(maxlen=50)
        self.time_data = deque(maxlen=50)
        
        # Create main frame
        main_frame = tk.Frame(root, bg='#f0f0f0')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel for calendar
        self.create_calendar_panel(main_frame)
        
        # Right panel for CPU usage
        self.create_cpu_panel(main_frame)
        
        # Start CPU monitoring thread
        self.running = True
        self.cpu_thread = threading.Thread(target=self.update_cpu_data, daemon=True)
        self.cpu_thread.start()
        
        # Start GUI update
        self.update_gui()
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def create_calendar_panel(self, parent):
        # Left frame for calendar
        left_frame = tk.Frame(parent, bg='white', relief=tk.RAISED, bd=2)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # Calendar title
        calendar_title = tk.Label(left_frame, text="日曆", font=('Arial', 16, 'bold'), 
                                bg='white', fg='#333')
        calendar_title.pack(pady=10)
        
        # Current date display
        today = datetime.date.today()
        date_str = today.strftime("%Y年%m月%d日 (%A)")
        
        self.date_label = tk.Label(left_frame, text=date_str, font=('Arial', 14), 
                                 bg='white', fg='#0066cc')
        self.date_label.pack(pady=5)
        
        # Calendar display
        cal_frame = tk.Frame(left_frame, bg='white')
        cal_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Create calendar
        self.create_calendar_widget(cal_frame, today)
    
    def create_calendar_widget(self, parent, today):
        # Get calendar data
        cal = calendar.monthcalendar(today.year, today.month)
        
        # Month and year header
        month_year = f"{today.year}年{today.month}月"
        month_label = tk.Label(parent, text=month_year, font=('Arial', 14, 'bold'),
                              bg='white', fg='#333')
        month_label.grid(row=0, column=0, columnspan=7, pady=10)
        
        # Weekday headers
        weekdays = ['一', '二', '三', '四', '五', '六', '日']
        for i, day in enumerate(weekdays):
            label = tk.Label(parent, text=day, font=('Arial', 12, 'bold'),
                           bg='#e0e0e0', fg='#333', width=4, height=1)
            label.grid(row=1, column=i, padx=1, pady=1, sticky='nsew')
        
        # Calendar days
        for week_num, week in enumerate(cal):
            for day_num, day in enumerate(week):
                if day == 0:
                    continue
                
                # Highlight today
                if day == today.day:
                    bg_color = '#0066cc'
                    fg_color = 'white'
                    font_weight = 'bold'
                else:
                    bg_color = 'white'
                    fg_color = '#333'
                    font_weight = 'normal'
                
                day_label = tk.Label(parent, text=str(day), 
                                   font=('Arial', 11, font_weight),
                                   bg=bg_color, fg=fg_color, width=4, height=2,
                                   relief=tk.FLAT, bd=1)
                day_label.grid(row=week_num+2, column=day_num, padx=1, pady=1, sticky='nsew')
    
    def create_cpu_panel(self, parent):
        # Right frame for CPU usage
        right_frame = tk.Frame(parent, bg='white', relief=tk.RAISED, bd=2)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # CPU title
        cpu_title = tk.Label(right_frame, text="CPU 使用率監控", font=('Arial', 16, 'bold'),
                           bg='white', fg='#333')
        cpu_title.pack(pady=10)
        
        # Current CPU usage display
        self.cpu_label = tk.Label(right_frame, text="CPU: 0%", font=('Arial', 20, 'bold'),
                                bg='white', fg='#ff6600')
        self.cpu_label.pack(pady=10)
        
        # CPU usage bar
        self.create_cpu_bar(right_frame)
        
        # CPU usage graph
        self.create_cpu_graph(right_frame)
    
    def create_cpu_bar(self, parent):
        bar_frame = tk.Frame(parent, bg='white')
        bar_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(bar_frame, text="即時使用率:", font=('Arial', 12),
                bg='white', fg='#333').pack(anchor=tk.W)
        
        # Progress bar for CPU usage
        self.cpu_progress = ttk.Progressbar(bar_frame, length=300, mode='determinate')
        self.cpu_progress.pack(pady=5, fill=tk.X)
        
        # CPU cores info
        cores = psutil.cpu_count()
        cores_label = tk.Label(bar_frame, text=f"CPU 核心數: {cores}", 
                              font=('Arial', 10), bg='white', fg='#666')
        cores_label.pack(anchor=tk.W, pady=5)
    
    def create_cpu_graph(self, parent):
        graph_frame = tk.Frame(parent, bg='white')
        graph_frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        
        # Create matplotlib figure
        self.fig = Figure(figsize=(6, 3), dpi=100, facecolor='white')
        self.ax = self.fig.add_subplot(111)
        
        # Configure plot
        self.ax.set_title('CPU 使用率歷史 (最近50秒)', fontsize=12, pad=20)
        self.ax.set_ylabel('使用率 (%)', fontsize=10)
        self.ax.set_xlabel('時間 (秒)', fontsize=10)
        self.ax.set_ylim(0, 100)
        self.ax.grid(True, alpha=0.3)
        
        # Create canvas
        self.canvas = FigureCanvasTkAgg(self.fig, graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Initialize plot line
        self.line, = self.ax.plot([], [], 'b-', linewidth=2, label='CPU %')
        self.ax.legend()
    
    def update_cpu_data(self):
        start_time = time.time()
        while self.running:
            try:
                cpu_percent = psutil.cpu_percent(interval=1)
                current_time = time.time() - start_time
                
                self.cpu_data.append(cpu_percent)
                self.time_data.append(current_time)
                
            except Exception as e:
                print(f"Error getting CPU data: {e}")
                time.sleep(1)
    
    def update_gui(self):
        if not self.running:
            return
            
        try:
            if self.cpu_data:
                current_cpu = self.cpu_data[-1]
                
                # Update CPU label
                self.cpu_label.config(text=f"CPU: {current_cpu:.1f}%")
                
                # Update progress bar
                self.cpu_progress['value'] = current_cpu
                
                # Update graph
                if len(self.cpu_data) > 1:
                    # Get relative time for x-axis
                    relative_times = [t - self.time_data[0] for t in self.time_data]
                    
                    self.line.set_data(relative_times, list(self.cpu_data))
                    
                    # Update x-axis range
                    if relative_times:
                        self.ax.set_xlim(max(0, relative_times[-1] - 50), relative_times[-1] + 2)
                    
                    self.canvas.draw_idle()
        
        except Exception as e:
            print(f"Error updating GUI: {e}")
        
        # Schedule next update
        self.root.after(1000, self.update_gui)
    
    def on_closing(self):
        self.running = False
        self.root.destroy()

def main():
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()