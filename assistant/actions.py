"""
MJ ASSISTANT - ACTIONS MODULE
All functions with Nepali + English support
"""

import webbrowser
import os
import datetime
import pyttsx3
import time
import pyautogui
import urllib.parse
import subprocess
import platform
import random
from pathlib import Path

# =====================================
# VOICE ENGINE INITIALIZATION
# =====================================

engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    """Speak text and print to console"""
    print(f"🤖 MJ: {text}")
    engine.say(text)
    engine.runAndWait()

# =====================================
# YOUTUBE CONTROLLER CLASS
# =====================================

class YouTubeController:
    def __init__(self):
        self.is_playing = False
        self.current_video = None
        self.volume_level = 50
        self.last_search = ""
        self.tab_count = 0
        
    def open_youtube_main(self):
        """Open YouTube in main tab"""
        webbrowser.open_new_tab("https://www.youtube.com")
        self.tab_count += 1
        speak("YouTube kholidiye")
        time.sleep(2)
        
    def open_new_youtube_tab(self):
        """Open YouTube in new tab"""
        webbrowser.open_new_tab("https://www.youtube.com")
        self.tab_count += 1
        speak("Arko YouTube tab kholidiye")
        time.sleep(1)
        
    def search_in_current_tab(self, query):
        """Search in current YouTube tab"""
        if not query:
            speak("Ke khojnu chahanchha?")
            return
        
        self.last_search = query
        speak(f"YouTube ma {query} khojdaichhu")
        
        try:
            # Click on search box
            pyautogui.click(x=500, y=150)
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            time.sleep(0.3)
            pyautogui.typewrite(query)
            time.sleep(0.5)
            pyautogui.press('enter')
            time.sleep(2)
            pyautogui.click(x=500, y=350)
            self.is_playing = True
            self.current_video = query
        except:
            # Fallback
            encoded = urllib.parse.quote(query)
            webbrowser.open(f"https://www.youtube.com/results?search_query={encoded}")
    
    def play_first_video(self):
        """Play first video"""
        try:
            pyautogui.click(x=500, y=350)
            self.is_playing = True
            speak("Pahilo video play garchhu")
        except:
            speak("Video play huna sakena")
    
    def play_next_video(self):
        """Next video"""
        pyautogui.hotkey('shift', 'n')
        speak("Arko video")
    
    def play_previous_video(self):
        """Previous video"""
        pyautogui.hotkey('shift', 'p')
        speak("Pahilo video")
    
    def close_youtube_tab(self):
        """Close current YouTube tab"""
        pyautogui.hotkey('ctrl', 'w')
        if self.tab_count > 0:
            self.tab_count -= 1
        speak("YouTube tab band gare")
    
    def switch_to_next_tab(self):
        """Switch to next tab"""
        pyautogui.hotkey('ctrl', 'tab')
        speak("Arko tab ma gayo")
    
    def switch_to_previous_tab(self):
        """Switch to previous tab"""
        pyautogui.hotkey('ctrl', 'shift', 'tab')
        speak("Pahilo tab ma gayo")
    
    def pause_video(self):
        """Pause video"""
        pyautogui.press('space')
        speak("Video rokidiye")
    
    def resume_video(self):
        """Resume video"""
        pyautogui.press('space')
        speak("Video feri chalayo")
    
    def volume_up(self):
        """Volume up"""
        if self.volume_level < 100:
            self.volume_level += 10
            for _ in range(3):
                pyautogui.press('up')
            speak(f"Volume {self.volume_level} percent")
    
    def volume_down(self):
        """Volume down"""
        if self.volume_level > 0:
            self.volume_level -= 10
            for _ in range(3):
                pyautogui.press('down')
            speak(f"Volume {self.volume_level} percent")
    
    def fullscreen(self):
        """Toggle fullscreen"""
        pyautogui.press('f')
        speak("Fullscreen gare")

# Create YouTube controller instance
yt = YouTubeController()

# =====================================
# YOUTUBE WRAPPER FUNCTIONS
# =====================================

def youtube_open():
    yt.open_youtube_main()

def youtube_new_tab():
    yt.open_new_youtube_tab()

def youtube_search(query):
    yt.search_in_current_tab(query)

def youtube_play_first():
    yt.play_first_video()

def youtube_next():
    yt.play_next_video()

def youtube_previous():
    yt.play_previous_video()

def youtube_close_tab():
    yt.close_youtube_tab()

def youtube_next_tab():
    yt.switch_to_next_tab()

def youtube_prev_tab():
    yt.switch_to_previous_tab()

def youtube_pause():
    yt.pause_video()

def youtube_resume():
    yt.resume_video()

def youtube_volume_up():
    yt.volume_up()

def youtube_volume_down():
    yt.volume_down()

def youtube_fullscreen():
    yt.fullscreen()

# =====================================
# WEBSITE FUNCTIONS
# =====================================

def open_website(site_name):
    """Open any website"""
    webbrowser.open(f"https://www.{site_name}.com")
    speak(f"{site_name} kholidiye")

def open_google():
    webbrowser.open("https://www.google.com")
    speak("Google kholidiye")

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    speak("YouTube kholidiye")

def open_chatgpt():
    webbrowser.open("https://chat.openai.com")
    speak("ChatGPT kholidiye")

def open_deepseek():
    webbrowser.open("https://chat.deepseek.com")
    speak("DeepSeek kholidiye")

def open_github():
    webbrowser.open("https://github.com")
    speak("GitHub kholidiye")

def open_gmail():
    webbrowser.open("https://mail.google.com")
    speak("Gmail kholidiye")

def open_facebook():
    webbrowser.open("https://facebook.com")
    speak("Facebook kholidiye")

def open_instagram():
    webbrowser.open("https://instagram.com")
    speak("Instagram kholidiye")

# =====================================
# SEARCH FUNCTIONS
# =====================================

def search_google(query):
    """Search on Google"""
    if not query:
        speak("Ke khojnu chahanchha?")
        return
    encoded = urllib.parse.quote(query)
    webbrowser.open(f"https://www.google.com/search?q={encoded}")
    speak(f"Google ma {query} khojdaichhu")

def search_youtube(query):
    """Search on YouTube"""
    if not query:
        speak("Ke khojnu chahanchha?")
        return
    encoded = urllib.parse.quote(query)
    webbrowser.open(f"https://www.youtube.com/results?search_query={encoded}")
    speak(f"YouTube ma {query} khojdaichhu")

# =====================================
# TIME FUNCTIONS
# =====================================

def tell_time():
    """Tell current time"""
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")
    speak(f"Time {time_str} bhayo")

def tell_date():
    """Tell current date"""
    now = datetime.datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")
    speak(f"Aaja {date_str} ho")

# =====================================
# SYSTEM FUNCTIONS
# =====================================

def shutdown_pc():
    """Shutdown computer"""
    speak("5 seconds ma PC band huncha")
    os.system("shutdown /s /t 5")

def restart_pc():
    """Restart computer"""
    speak("5 seconds ma PC restart huncha")
    os.system("shutdown /r /t 5")

def lock_pc():
    """Lock computer"""
    speak("PC lock gare")
    os.system("rundll32.exe user32.dll,LockWorkStation")

def volume_up():
    """System volume up"""
    for _ in range(5):
        pyautogui.press('volumeup')
    speak("Volume badhaudiye")

def volume_down():
    """System volume down"""
    for _ in range(5):
        pyautogui.press('volumedown')
    speak("Volume ghataudiye")

def volume_mute():
    """Mute volume"""
    pyautogui.press('volumemute')
    speak("Volume mute gare")

# =====================================
# APP FUNCTIONS
# =====================================

def open_notepad():
    os.system("start notepad.exe")
    speak("Notepad kholidiye")

def open_calculator():
    os.system("start calc.exe")
    speak("Calculator kholidiye")

def open_cmd():
    os.system("start cmd.exe")
    speak("Command Prompt kholidiye")

def open_chrome():
    os.system("start chrome.exe")
    speak("Chrome kholidiye")

# =====================================
# SCREENSHOT FUNCTION
# =====================================

def take_screenshot():
    """Take screenshot"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        speak(f"Screenshot save gare: {filename}")
    except:
        speak("Screenshot lina sakina")

# =====================================
# CONVERSATION FUNCTIONS
# =====================================

def thank_you():
    responses = [
        "Timilai pani dhanyabad",
        "Kehi chaincha bhane bhanu hai",
        "Khushi lagyo timilai help garna",
    ]
    speak(random.choice(responses))

def how_are_you():
    responses = [
        "Ma thik chu, timi kasto chhau?",
        "Ready to help you",
        "Perfect, timi chinta nagara",
    ]
    speak(random.choice(responses))

def greet_morning():
    speak("Good morning Gulshan, subha prabhat")

def greet_night():
    speak("Good night Gulshan, mitho nindra")

def tell_joke():
    jokes = [
        "Kina computer chiso huncha? Because it has Windows!",
        "Programmer haru kina sadhai busy huncha? Because they have too many problems!",
    ]
    speak(random.choice(jokes))

def introduce():
    speak("Ma MJ hu, Gulshan ko personal assistant. Ke help chahanchha?")

def show_help():
    help_text = "MJ lai command dinu hola: YouTube khol, search gar, time batau, window band gara, volume control"
    speak(help_text)