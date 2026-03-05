import webbrowser
import os
import datetime
import pyttsx3
import platform
import subprocess
import pyautogui
import time

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)
engine.setProperty('voice', 'english')  # Use female voice if available

def speak(text):
    print(f"MJ: {text}")
    engine.say(text)
    engine.runAndWait()

# =====================================
# 1️⃣ OPEN YOUTUBE
# =====================================
def open_youtube():
    try:
        webbrowser.open("https://www.youtube.com")
    except:
        os.system("start https://www.youtube.com")

# =====================================
# 2️⃣ PLAY MUSIC
# =====================================
def play_music():
    webbrowser.open("https://music.youtube.com")

# =====================================
# 3️⃣ WHAT TIME IS IT
# =====================================
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The time is {current_time}")

# =====================================
# 4️⃣ SEARCH GOOGLE
# =====================================
def search_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

# =====================================
# 5️⃣ SYSTEM CONTROL
# =====================================
def shutdown_pc():
    os.system("shutdown /s /t 5")

def restart_pc():
    os.system("shutdown /r /t 5")

# =====================================
# 6️⃣ CLOSE WINDOW/TAB (ALL VARIATIONS)
# =====================================
def close_window():
    """Close current window/tab using keyboard shortcut"""
    try:
        # Try multiple methods to ensure it works
        pyautogui.hotkey('alt', 'f4')  # Close window
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'w')   # Close tab (if browser)
        speak("Closed")
    except:
        try:
            # Alternative method
            import keyboard
            keyboard.press_and_release('alt+f4')
        except:
            speak("Could not close")

def close_all():
    """Close all windows (emergency)"""
    try:
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im msedge.exe")
        os.system("taskkill /f /im firefox.exe")
        speak("All windows closed")
    except:
        speak("Close command failed")