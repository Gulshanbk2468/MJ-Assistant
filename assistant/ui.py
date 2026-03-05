import tkinter as tk
from tkinter import scrolledtext
import threading
import datetime
import psutil
import time
import os
from assistant.brain import run_brain
from assistant.utils import get_greeting

class MJ_UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MJ Terminal v2.0")
        self.root.geometry("1200x700")
        self.root.configure(bg="#0a0a0a")
        
        # Set minimum window size
        self.root.minsize(1000, 600)
        
        # Create main container
        self.setup_ui()
        
        # Start brain in background
        self.activated = False
        threading.Thread(target=self.start_brain, daemon=True).start()
        
        # Start system monitor
        self.update_system_stats()
        
        self.root.mainloop()
    
    def setup_ui(self):
        """Setup clean professional UI"""
        
        # ========== LEFT PANEL (SYSTEM INFO) ==========
        left_frame = tk.Frame(self.root, bg="#0a0a0a", width=300)
        left_frame.pack(side="left", fill="y", padx=10, pady=10)
        left_frame.pack_propagate(False)
        
        # MJ Logo / Title
        title = tk.Label(
            left_frame,
            text="⚡ MJ v2.0 ⚡",
            font=("Consolas", 18, "bold"),
            fg="#00ff00",
            bg="#0a0a0a"
        )
        title.pack(pady=(20, 30))
        
        # System Status Box
        status_frame = tk.Frame(left_frame, bg="#1a1a1a", relief="solid", bd=1)
        status_frame.pack(fill="x", pady=10)
        
        tk.Label(
            status_frame,
            text="SYSTEM STATUS",
            font=("Consolas", 10, "bold"),
            fg="#00ff00",
            bg="#1a1a1a"
        ).pack(pady=5)
        
        self.status_indicator = tk.Label(
            status_frame,
            text="● AWAITING ACTIVATION",
            font=("Consolas", 9),
            fg="#ffaa00",
            bg="#1a1a1a"
        )
        self.status_indicator.pack(pady=5)
        
        # System Stats
        stats_frame = tk.Frame(left_frame, bg="#1a1a1a", relief="solid", bd=1)
        stats_frame.pack(fill="x", pady=10)
        
        tk.Label(
            stats_frame,
            text="SYSTEM METRICS",
            font=("Consolas", 10, "bold"),
            fg="#00ff00",
            bg="#1a1a1a"
        ).pack(pady=5)
        
        self.cpu_label = tk.Label(
            stats_frame,
            text="CPU: --%",
            font=("Consolas", 9),
            fg="#00ff00",
            bg="#1a1a1a",
            anchor="w"
        )
        self.cpu_label.pack(pady=2, padx=10, fill="x")
        
        self.ram_label = tk.Label(
            stats_frame,
            text="RAM: --%",
            font=("Consolas", 9),
            fg="#00ff00",
            bg="#1a1a1a",
            anchor="w"
        )
        self.ram_label.pack(pady=2, padx=10, fill="x")
        
        self.uptime_label = tk.Label(
            stats_frame,
            text="UPTIME: --:--:--",
            font=("Consolas", 9),
            fg="#00ff00",
            bg="#1a1a1a",
            anchor="w"
        )
        self.uptime_label.pack(pady=2, padx=10, fill="x")
        
        # Quick Commands
        commands_frame = tk.Frame(left_frame, bg="#1a1a1a", relief="solid", bd=1)
        commands_frame.pack(fill="both", expand=True, pady=10)
        
        tk.Label(
            commands_frame,
            text="QUICK COMMANDS",
            font=("Consolas", 10, "bold"),
            fg="#00ff00",
            bg="#1a1a1a"
        ).pack(pady=5)
        
        commands = [
            "🎤 'hey mj' - Activate",
            "▶ 'open youtube'",
            "▶ 'play music'",
            "▶ 'what time'",
            "▶ 'search [query]'",
            "▶ 'shutdown' / 'restart'",
            "━━━━━━━━━━━━━━━━",
            "❌ CLOSE COMMANDS:",
            "  • 'okay close it mj'",
            "  • 'mj close it'",
            "  • 'close it mj'",
            "  • 'mj close'",
            "  • 'close mj'",
            "━━━━━━━━━━━━━━━━",
            "💤 'deactivate'",
            "👋 'exit' / 'quit'"
        ]
        
        for cmd in commands:
            if "━━━" in cmd:
                tk.Label(
                    commands_frame,
                    text=cmd,
                    font=("Consolas", 8),
                    fg="#666666",
                    bg="#1a1a1a"
                ).pack()
            elif "CLOSE" in cmd or "❌" in cmd:
                tk.Label(
                    commands_frame,
                    text=cmd,
                    font=("Consolas", 8, "bold"),
                    fg="#ff6666",
                    bg="#1a1a1a"
                ).pack(pady=1)
            else:
                tk.Label(
                    commands_frame,
                    text=cmd,
                    font=("Consolas", 8),
                    fg="#00ff00",
                    bg="#1a1a1a"
                ).pack(pady=1)
        
        # ========== RIGHT PANEL (TERMINAL) ==========
        right_frame = tk.Frame(self.root, bg="#0a0a0a")
        right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        
        # Terminal Header
        header_frame = tk.Frame(right_frame, bg="#1a1a1a", height=30)
        header_frame.pack(fill="x", pady=(0, 5))
        header_frame.pack_propagate(False)
        
        tk.Label(
            header_frame,
            text="MJ COMMAND TERMINAL",
            font=("Consolas", 11, "bold"),
            fg="#00ff00",
            bg="#1a1a1a"
        ).pack(side="left", padx=10, pady=5)
        
        self.time_label = tk.Label(
            header_frame,
            text=datetime.datetime.now().strftime("%H:%M:%S"),
            font=("Consolas", 10),
            fg="#666666",
            bg="#1a1a1a"
        )
        self.time_label.pack(side="right", padx=10, pady=5)
        
        # Terminal Output
        self.terminal = scrolledtext.ScrolledText(
            right_frame,
            bg="#0a0a0a",
            fg="#00ff00",
            font=("Consolas", 10),
            insertbackground="#00ff00",
            wrap=tk.WORD,
            borderwidth=0,
            highlightthickness=1,
            highlightcolor="#333333",
            highlightbackground="#333333"
        )
        self.terminal.pack(fill="both", expand=True)
        
        # Configure terminal tags
        self.terminal.tag_config("prompt", foreground="#00ff00")
        self.terminal.tag_config("command", foreground="#ffffff")
        self.terminal.tag_config("error", foreground="#ff6666")
        self.terminal.tag_config("success", foreground="#66ff66")
        self.terminal.tag_config("system", foreground="#ffaa00")
        self.terminal.tag_config("close", foreground="#ff6666", font=("Consolas", 10, "bold"))
        
        # Input field at bottom
        input_frame = tk.Frame(right_frame, bg="#1a1a1a", height=30)
        input_frame.pack(fill="x", pady=(5, 0))
        input_frame.pack_propagate(False)
        
        tk.Label(
            input_frame,
            text=">",
            font=("Consolas", 10, "bold"),
            fg="#00ff00",
            bg="#1a1a1a"
        ).pack(side="left", padx=5)
        
        self.input_field = tk.Entry(
            input_frame,
            bg="#1a1a1a",
            fg="#00ff00",
            font=("Consolas", 10),
            insertbackground="#00ff00",
            borderwidth=0,
            highlightthickness=0
        )
        self.input_field.pack(side="left", fill="x", expand=True, padx=5)
        self.input_field.bind("<Return>", self.send_command)
        
        # Initial logs
        self.log("╔════════════════════════════════════════╗", "system")
        self.log("║        MJ TERMINAL v2.0               ║", "system")
        self.log("║        System Online                   ║", "system")
        self.log("╚════════════════════════════════════════╝", "system")
        self.log("")
        self.log(f"🎯 {get_greeting()}", "success")
        self.log("")
        self.log("⚡ Say 'hey mj' to activate voice control", "system")
        self.log("💬 Or type commands directly in the input field", "system")
        self.log("")
    
    def send_command(self, event):
        """Handle manual command input"""
        command = self.input_field.get().strip().lower()
        self.input_field.delete(0, tk.END)
        
        if command:
            self.log(f"⌨️ Manual: {command}", "command")
            
            if command in ["exit", "quit"]:
                self.log("👋 Shutting down...", "system")
                self.root.after(1000, self.root.quit)
            elif command == "clear":
                self.terminal.delete(1.0, tk.END)
            else:
                # Pass to brain for processing
                self.log(f"🤖 Processing: {command}", "system")
    
    def log(self, message, tag=None):
        """Add message to terminal"""
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        prefix = f"[{timestamp}] "
        
        self.terminal.insert(tk.END, prefix, "prompt")
        
        if tag:
            self.terminal.insert(tk.END, f"{message}\n", tag)
        else:
            self.terminal.insert(tk.END, f"{message}\n")
        
        self.terminal.see(tk.END)
    
    def update_activation_status(self, activated):
        """Update UI based on activation state"""
        self.activated = activated
        if activated:
            self.status_indicator.config(
                text="● ACTIVE - LISTENING",
                fg="#00ff00"
            )
            self.log("🎤 MJ activated - listening for commands", "success")
        else:
            self.status_indicator.config(
                text="● AWAITING ACTIVATION",
                fg="#ffaa00"
            )
    
    def update_system_stats(self):
        """Update system statistics"""
        try:
            # CPU and RAM usage
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            
            # Uptime
            boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
            uptime = datetime.datetime.now() - boot_time
            uptime_str = str(uptime).split('.')[0]  # Remove microseconds
            
            self.cpu_label.config(text=f"CPU: {cpu}%")
            self.ram_label.config(text=f"RAM: {ram}%")
            self.uptime_label.config(text=f"UPTIME: {uptime_str}")
            
            # Update time
            self.time_label.config(text=datetime.datetime.now().strftime("%H:%M:%S"))
            
        except:
            pass
        
        # Update every 2 seconds
        self.root.after(2000, self.update_system_stats)
    
    def handle_close_command(self):
        """Handle close commands in UI"""
        self.log("❌ Executing close command...", "close")
        try:
            import pyautogui
            pyautogui.hotkey('alt', 'f4')
            self.log("✅ Window closed", "success")
        except:
            self.log("⚠️ Could not close window", "error")
    
    def start_brain(self):
        """Start MJ brain with UI callbacks"""
        run_brain(self.log, self.update_activation_status, self.handle_close_command)

def launch_ui():
    MJ_UI()