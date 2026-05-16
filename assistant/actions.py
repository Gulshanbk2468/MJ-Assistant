"""
MJ ASSISTANT - ACTIONS MODULE
FINAL VERSION - All functions with voice replies
"""

import webbrowser
import os
import datetime
import pyttsx3
import time
import pyautogui
import urllib.parse
import random
from assistant.utils import *

# =====================================
# VOICE ENGINE
# =====================================

engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

def speak(text):
    """Speak text with emotion"""
    print(f"🤖 MJ: {text}")
    engine.say(text)
    engine.runAndWait()

# =====================================
# WINDOW MANAGEMENT
# =====================================

def close_current_window():
    """Close current window with voice"""
    try:
        pyautogui.hotkey('alt', 'f4')
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'w')
        speak("Window closed.")
        return True
    except:
        try:
            os.system("taskkill /f /im chrome.exe")
            os.system("taskkill /f /im msedge.exe")
            speak("Window closed.")
            return True
        except:
            speak("Unable to close window.")
            return False

# =====================================
# SMART WEBSITE CONTROL
# =====================================

# ADD YOUR CUSTOM URLS HERE
WEBSITES = {

    "facebook": "https://facebook.com",
    "fb": "https://facebook.com",

    "gmail": "https://mail.google.com",
    "email": "https://mail.google.com",

    "instagram": "https://instagram.com",

    "youtube": "https://youtube.com",

    "chatgpt": "https://chat.openai.com",

    # ADD MORE LIKE THIS
    # "github": "https://github.com",
    # "twitter": "https://twitter.com",
}

opened_tabs = {}

def smart_open_website(command):
    """
    Open websites using voice commands
    """

    global opened_tabs

    command = command.lower()

    for name, url in WEBSITES.items():

        if name in command:

            webbrowser.open(url)

            opened_tabs[name] = True

            speak(f"Opening {name} for you Gulshan.")

            return True

    return False


def smart_close_website(command):
    """
    Close specific website tab
    """

    command = command.lower()

    try:

        # ===== GMAIL =====
        if "gmail" in command or "email" in command:

            pyautogui.hotkey('ctrl', '1')
            time.sleep(0.4)
            pyautogui.hotkey('ctrl', 'w')

            speak("Closing Gmail tab.")
            return True

        # ===== FACEBOOK =====
        elif "facebook" in command or "fb" in command:

            pyautogui.hotkey('ctrl', '2')
            time.sleep(0.4)
            pyautogui.hotkey('ctrl', 'w')

            speak("Closing Facebook tab.")
            return True

        # ===== INSTAGRAM =====
        elif "instagram" in command:

            pyautogui.hotkey('ctrl', '3')
            time.sleep(0.4)
            pyautogui.hotkey('ctrl', 'w')

            speak("Closing Instagram tab.")
            return True

        # ===== YOUTUBE =====
        elif "youtube" in command:

            pyautogui.hotkey('ctrl', '4')
            time.sleep(0.4)
            pyautogui.hotkey('ctrl', 'w')

            speak("Closing YouTube tab.")
            return True

        # ===== CHATGPT =====
        elif "chatgpt" in command:

            pyautogui.hotkey('ctrl', '5')
            time.sleep(0.4)
            pyautogui.hotkey('ctrl', 'w')

            speak("Closing ChatGPT tab.")
            return True

        return False

    except:
        speak("Unable to close tab.")
        return False

# =====================================
# YOUTUBE FUNCTIONS
# =====================================

def youtube_open():
    """Open YouTube"""
    webbrowser.open("https://www.youtube.com")
    speak("Opening YouTube for you Gulshan.")

def youtube_play_nepali(song_name=""):
    """Play Nepali song"""
    if song_name:
        query = f"{song_name} nepali song"
    else:
        nepali_songs = [
            "Resham Firiri",
            "Mutu Bhanda Mitho",
            "Sirf Timi",
            "Samhalinchu"
        ]
        query = random.choice(nepali_songs)

    webbrowser.open(
        f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    )

    speak(f"Playing {query} for you Gulshan.")

def youtube_play_bollywood(song_name=""):
    """Play Bollywood song"""

    if song_name:
        query = f"{song_name} bollywood song"
    else:
        bollywood_songs = [
            "Tum Hi Ho",
            "Kesariya",
            "Channa Mereya",
            "Kalank"
        ]
        query = random.choice(bollywood_songs)

    webbrowser.open(
        f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
    )

    speak(f"Playing {query} for you Gulshan.")

def youtube_play_artist(artist_name):
    """Play artist songs"""

    webbrowser.open(
        f"https://www.youtube.com/results?search_query={urllib.parse.quote(artist_name + ' songs')}"
    )

    speak(f"Playing {artist_name} songs for you Gulshan.")

def youtube_play_song(song_name):
    """Play specific song"""

    webbrowser.open(
        f"https://www.youtube.com/results?search_query={urllib.parse.quote(song_name)}"
    )

    speak(f"Playing {song_name} for you Gulshan.")

def youtube_pause():
    """Pause video"""

    pyautogui.press('space')
    speak("Video paused.")

def youtube_resume():
    """Resume video"""

    pyautogui.press('space')
    speak("Video resumed.")

def youtube_next():
    """Next video"""

    pyautogui.hotkey('shift', 'n')
    speak("Next video.")

def youtube_previous():
    """Previous video"""

    pyautogui.hotkey('shift', 'p')
    speak("Previous video.")

def youtube_volume_up():
    """Volume up"""

    for _ in range(3):
        pyautogui.press('up')

    speak("Volume increased.")

def youtube_volume_down():
    """Volume down"""

    for _ in range(3):
        pyautogui.press('down')

    speak("Volume decreased.")

def youtube_fullscreen():
    """Fullscreen"""

    pyautogui.press('f')
    speak("Fullscreen mode.")

# =====================================
# WEBSITE FUNCTIONS
# =====================================

def open_google():
    webbrowser.open("https://www.google.com")
    speak("Opening Google for you Gulshan.")

def open_chatgpt():
    webbrowser.open("https://chat.openai.com")
    speak("Opening ChatGPT.")

def open_facebook():
    webbrowser.open("https://facebook.com")
    speak("Opening Facebook.")

def open_instagram():
    webbrowser.open("https://instagram.com")
    speak("Opening Instagram.")

def open_gmail():
    webbrowser.open("https://mail.google.com")
    speak("Opening Gmail.")

# =====================================
# TIME FUNCTIONS
# =====================================

def tell_time():

    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")

    speak(f"The time is {time_str}.")

def tell_date():

    now = datetime.datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")

    speak(f"Today is {date_str}.")

# =====================================
# SYSTEM FUNCTIONS
# =====================================

def take_screenshot():

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshot_{timestamp}.png"

    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)

        speak(f"Screenshot saved as {filename}.")

    except:
        speak("Unable to take screenshot.")

def shutdown_pc():

    speak("Shutting down your computer in 5 seconds. Goodbye Gulshan!")
    os.system("shutdown /s /t 5")

def restart_pc():

    speak("Restarting your computer in 5 seconds. See you soon Gulshan!")
    os.system("shutdown /r /t 5")

def lock_pc():

    speak("Locking your computer.")
    os.system("rundll32.exe user32.dll,LockWorkStation")

# =====================================
# CONVERSATION FUNCTIONS
# =====================================

def thank_you():

    responses = [
        "You're welcome Gulshan!",
        "Happy to help Gulshan!",
        "Anytime Gulshan!",
        "My pleasure Gulshan!"
    ]

    speak(random.choice(responses))

def how_are_you():

    responses = [
        "I'm doing great Gulshan! Ready to help you.",
        "All systems operational Gulshan!",
        "I'm perfect Gulshan! What can I do for you?"
    ]

    speak(random.choice(responses))

def tell_joke():

    jokes = [
        "Why do computers get cold? Because they leave their Windows open!",
        "Why did the programmer quit his job? He didn't get arrays!",
        "What's a computer's favorite beat? An an-nvidia beat!"
    ]

    speak(random.choice(jokes))

def introduce():

    intro = f"""
    Hello Gulshan! I am MJ, your personal AI assistant.
    I can open websites, play YouTube videos, control your computer,
    tell you the time, take screenshots, and much more.
    Just say a command and I'll take care of it.
    How can I help you today Gulshan?
    """

    speak(intro)

def show_help():

    help_text = """
    Here are the commands you can use:

    - 'facebook open gar'
    - 'gmail khola'
    - 'youtube open'
    - 'close this email tab'
    - 'close facebook'
    - 'close it'

    - 'open youtube'
    - 'nepali song'
    - 'bollywood song'
    - 'play [song name]'
    - 'pause'
    - 'next'
    - 'volume up'

    - 'google khol'
    - 'time kati bhayo'
    - 'screenshot'
    - 'who are you'
    - 'help'
    """

    speak(help_text)