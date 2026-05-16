"""
MJ ASSISTANT - ULTIMATE UI
Cyberpunk Terminal Design
"""

import tkinter as tk
from tkinter import scrolledtext, font
import threading
import datetime
import random
import time
from assistant.brain import run_brain
from assistant.utils import get_greeting

class MJ_UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MJ ULTIMATE ASSISTANT")
        self.root.geometry("1200x700")
        self.root.configure(bg="#0a0f1a")
        
        # Make window frameless for cyberpunk look
        self.root.overrideredirect(True)
        
        # Center window on screen
        self.center_window()
        
        # Enable dragging
        self.root.bind('<Button-1>', self.start_move)
        self.root.bind('<B1-Motion>', self.on_move)
        
        # Create main frame
        self.create_ui()
        
        # Animation variables
        self.pulse_value = 0
        self.pulse_direction = 1
        
        # Start animations
        self.animate()
        
        # Start brain
        threading.Thread(target=self.start_brain, daemon=True).start()
        
        self.root.mainloop()
    
    def center_window(self):
        """Center window on screen"""
        self.root.update_idletasks()
        width = 1200
        height = 700
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
    
    def create_ui(self):
        """Create ultimate cyberpunk UI"""
        
        # ========== TOP BAR ==========
        top_bar = tk.Frame(self.root, bg="#1a1f2e", height=40)
        top_bar.pack(fill="x")
        top_bar.pack_propagate(False)
        
        # Title with glitch effect
        title_label = tk.Label(
            top_bar,
            text="⚡ MJ TERMINAL v3.0 ⚡",
            font=("Courier New", 14, "bold"),
            fg="#00ffff",
            bg="#1a1f2e"
        )
        title_label.pack(side="left", padx=15, pady=8)
        
        # System time
        self.time_label = tk.Label(
            top_bar,
            text="",
            font=("Courier New", 12),
            fg="#00ffaa",
            bg="#1a1f2e"
        )
        self.time_label.pack(side="right", padx=15, pady=8)
        
        # Close button
        close_btn = tk.Button(
            top_bar,
            text="✕",
            font=("Arial", 12, "bold"),
            fg="#ff5555",
            bg="#1a1f2e",
            bd=0,
            activebackground="#ff5555",
            activeforeground="white",
            command=self.root.quit
        )
        close_btn.pack(side="right", padx=5)
        
        # Minimize button
        min_btn = tk.Button(
            top_bar,
            text="─",
            font=("Arial", 12, "bold"),
            fg="#ffff00",
            bg="#1a1f2e",
            bd=0,
            activebackground="#ffff00",
            activeforeground="black",
            command=self.minimize_window
        )
        min_btn.pack(side="right", padx=5)
        
        # ========== MAIN CONTENT ==========
        main_frame = tk.Frame(self.root, bg="#0a0f1a")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Left Panel - System Status
        left_panel = tk.Frame(main_frame, bg="#151e2a", width=250)
        left_panel.pack(side="left", fill="y", padx=(0, 10))
        left_panel.pack_propagate(False)
        
        # MJ Logo
        logo_frame = tk.Frame(left_panel, bg="#151e2a", height=100)
        logo_frame.pack(fill="x", pady=20)
        logo_frame.pack_propagate(False)
        
        logo_text = tk.Label(
            logo_frame,
            text="███╗   ███╗     ██╗\n████╗ ████║     ██║\n██╔████╔██║     ██║\n██║╚██╔╝██║██╗  ██║\n██║ ╚═╝ ██║╚█████╔╝\n╚═╝     ╚═╝ ╚════╝",
            font=("Courier New", 8),
            fg="#00ffaa",
            bg="#151e2a",
            justify="center"
        )
        logo_text.pack()
        
        # Status indicators
        status_frame = tk.Frame(left_panel, bg="#1f2a36", bd=1, relief="solid")
        status_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(
            status_frame,
            text="SYSTEM STATUS",
            font=("Courier New", 10, "bold"),
            fg="#00ffff",
            bg="#1f2a36"
        ).pack(pady=5)
        
        self.status_indicator = tk.Label(
            status_frame,
            text="● AWAITING ACTIVATION",
            font=("Courier New", 9),
            fg="#ffaa00",
            bg="#1f2a36"
        )
        self.status_indicator.pack(pady=5)
        
        # System stats
        stats_frame = tk.Frame(left_panel, bg="#1f2a36", bd=1, relief="solid")
        stats_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(
            stats_frame,
            text="SYSTEM METRICS",
            font=("Courier New", 10, "bold"),
            fg="#00ffff",
            bg="#1f2a36"
        ).pack(pady=5)
        
        self.cpu_label = tk.Label(
            stats_frame,
            text="CPU: --%",
            font=("Courier New", 9),
            fg="#00ffaa",
            bg="#1f2a36",
            anchor="w"
        )
        self.cpu_label.pack(pady=2, padx=10, fill="x")
        
        self.ram_label = tk.Label(
            stats_frame,
            text="RAM: --%",
            font=("Courier New", 9),
            fg="#00ffaa",
            bg="#1f2a36",
            anchor="w"
        )
        self.ram_label.pack(pady=2, padx=10, fill="x")
        
        # Quick commands
        quick_frame = tk.Frame(left_panel, bg="#1f2a36", bd=1, relief="solid")
        quick_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        tk.Label(
            quick_frame,
            text="QUICK COMMANDS",
            font=("Courier New", 10, "bold"),
            fg="#00ffff",
            bg="#1f2a36"
        ).pack(pady=5)
        
        commands = [
            "🎵 'nepali song'",
            "🎵 'bollywood song'",
            "🎵 'arijit singh'",
            "🪟 'close it'",
            "🌐 'google khol'",
            "🌐 'chatgpt khol'",
            "⏰ 'time kati bhayo'",
            "📸 'screenshot le'",
            "😊 'joke sunau'",
            "❓ 'help'"
        ]
        
        for cmd in commands:
            tk.Label(
                quick_frame,
                text=cmd,
                font=("Courier New", 8),
                fg="#88aaff",
                bg="#1f2a36",
                anchor="w"
            ).pack(pady=2, padx=10, fill="x")
        
        # Right Panel - Terminal
        right_panel = tk.Frame(main_frame, bg="#0f1420")
        right_panel.pack(side="right", fill="both", expand=True)
        
        # Terminal header
        term_header = tk.Frame(right_panel, bg="#1f2a36", height=30)
        term_header.pack(fill="x")
        term_header.pack_propagate(False)
        
        tk.Label(
            term_header,
            text="➤ MJ COMMAND TERMINAL",
            font=("Courier New", 10, "bold"),
            fg="#00ffaa",
            bg="#1f2a36"
        ).pack(side="left", padx=10, pady=5)
        
        # Terminal output
        self.terminal = scrolledtext.ScrolledText(
            right_panel,
            bg="#0a0f1a",
            fg="#00ffaa",
            font=("Courier New", 10),
            insertbackground="#00ffff",
            wrap=tk.WORD,
            borderwidth=0,
            highlightthickness=1,
            highlightcolor="#2a3a4a",
            highlightbackground="#2a3a4a"
        )
        self.terminal.pack(fill="both", expand=True, pady=(5, 0))
        
        # Configure tags for colored output
        self.terminal.tag_config("command", foreground="#ffffff", font=("Courier New", 10, "bold"))
        self.terminal.tag_config("success", foreground="#66ff66")
        self.terminal.tag_config("error", foreground="#ff6666")
        self.terminal.tag_config("close", foreground="#ffaa66")
        self.terminal.tag_config("system", foreground="#88aaff")
        self.terminal.tag_config("highlight", foreground="#ffff00", font=("Courier New", 10, "bold"))
        
        # Input field
        input_frame = tk.Frame(right_panel, bg="#1f2a36", height=35)
        input_frame.pack(fill="x", pady=(5, 0))
        input_frame.pack_propagate(False)
        
        prompt_label = tk.Label(
            input_frame,
            text="❯",
            font=("Courier New", 12, "bold"),
            fg="#00ffff",
            bg="#1f2a36"
        )
        prompt_label.pack(side="left", padx=10)
        
        self.input_field = tk.Entry(
            input_frame,
            bg="#0a0f1a",
            fg="#00ffaa",
            font=("Courier New", 10),
            insertbackground="#00ffff",
            borderwidth=0,
            highlightthickness=1,
            highlightcolor="#2a3a4a",
            highlightbackground="#2a3a4a"
        )
        self.input_field.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.input_field.bind("<Return>", self.send_command)
        
        # Initial logs
        self.log("╔════════════════════════════════════════════════╗", "system")
        self.log("║  MJ ULTIMATE ASSISTANT v3.0                    ║", "system")
        self.log("║     ███╗   ███╗     ██╗                        ║", "system")
        self.log("║     ████╗ ████║     ██║                        ║", "system")
        self.log("║     ██╔████╔██║     ██║                        ║", "system")
        self.log("║     ██║╚██╔╝██║██╗  ██║                        ║", "system")
        self.log("║     ██║ ╚═╝ ██║╚█████╔╝                        ║", "system")
        self.log("║     ╚═╝     ╚═╝ ╚════╝                         ║", "system")
        self.log("╚════════════════════════════════════════════════╝", "system")
        self.log("")
        
        # Welcome message
        welcome = get_greeting()
        self.log(f"🎯 {welcome}", "highlight")
        self.log("")
        self.log("⚡ Say 'hey mj' to activate voice control", "system")
        self.log("💬 Type 'help' for available commands", "system")
        self.log("")
        self.log("➤ System ready. Waiting for input...", "success")
        
        # Start system monitor
        self.update_stats()
        self.update_time()
    
    def log(self, message, tag=None):
        """Add message to terminal with optional tag"""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        if tag:
            self.terminal.insert(tk.END, f"[{timestamp}] {message}\n", tag)
        else:
            self.terminal.insert(tk.END, f"[{timestamp}] {message}\n")
        
        self.terminal.see(tk.END)
        self.root.update()
    
    def update_status(self, activated):
        """Update status indicator"""
        if activated:
            self.status_indicator.config(text="● ACTIVE - LISTENING", fg="#00ff00")
            self.log("🎤 Voice control activated", "success")
        else:
            self.status_indicator.config(text="● AWAITING ACTIVATION", fg="#ffaa00")
    
    def update_stats(self):
        """Update system statistics"""
        try:
            import psutil
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            
            self.cpu_label.config(text=f"CPU: {cpu}%")
            self.ram_label.config(text=f"RAM: {ram}%")
        except:
            pass
        
        self.root.after(2000, self.update_stats)
    
    def update_time(self):
        """Update time display"""
        current = datetime.datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=current)
        self.root.after(1000, self.update_time)
    
    def animate(self):
        """Animate UI elements"""
        self.pulse_value += self.pulse_direction * 5
        if self.pulse_value >= 100 or self.pulse_value <= 0:
            self.pulse_direction *= -1
        
        # Update status indicator pulse
        self.root.after(50, self.animate)
    
    def minimize_window(self):
        """Minimize window"""
        self.root.iconify()
    
    def send_command(self, event):
        """Handle manual command input"""
        command = self.input_field.get().strip()
        self.input_field.delete(0, tk.END)
        
        if command:
            self.log(f"⌨️ Manual: {command}", "command")
            # You can add manual command processing here
    
    def start_brain(self):
        """Start brain in background"""
        run_brain(self.log, self.update_status, lambda: None)

def launch_ui():
    MJ_UI()