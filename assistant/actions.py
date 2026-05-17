"""
MJ ASSISTANT - ACTIONS MODULE
FINAL VERSION - SMART WEBSITE CONTROL + AI SEARCH + TAB MANAGEMENT
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

# =====================================
# TAB MEMORY
# =====================================

opened_tabs = []

last_opened_tab = None

# =====================================
# SMART RESPONSE SYSTEM
# =====================================

OPENING_RESPONSES = [

    "Okay Gulshan, मैले {name} open गरिदिएको छु.",
    
    "Sure Gulshan, {name} अहिले open हुँदैछ.",

    "Done Gulshan, {name} ready छ.",

    "Opening {name} right away Gulshan.",

    "Alright Gulshan, launching {name}.",

    "Your {name} is now open Gulshan.",

    "Here you go Gulshan, {name} खोल्दैछु.",

    "Working on it Gulshan, {name} खुलिरहेको छ.",

]

CLOSING_RESPONSES = [

    "Okay Gulshan, {name} बन्द गरिदिएको छु.",

    "{name} successfully close भयो.",

    "Done Gulshan, {name} closed.",

    "Closing {name} for you Gulshan.",

    "{name} tab अहिले बन्द भयो Gulshan."

]

ERROR_RESPONSES = [

    "Sorry Gulshan, मैले बुझिन.",

    "Please repeat the command Gulshan.",

    "Unable to process your request Gulshan.",

    "Again भन्नुहोस् Gulshan."

]

SUCCESS_RESPONSES = [

    "Done Gulshan.",

    "Task completed successfully.",

    "काम सम्पन्न भयो Gulshan.",

    "Everything is ready Gulshan."

]

# =====================================
# SPEAK FUNCTION
# =====================================

def speak(text):
    """
    Speak text
    """

    print(f"🤖 MJ: {text}")

    engine.say(text)

    engine.runAndWait()

# =====================================
# SMART RANDOM REPLY
# =====================================

def smart_reply(reply_list, name=""):

    response = random.choice(reply_list)

    response = response.format(name=name)

    speak(response)

# =====================================
# SMART WEBSITE OPEN
# =====================================

def smart_open_website(command):
    """
    Smart website open system
    """

    global last_opened_tab

    try:

        query = command.lower().strip()

        # remove open keywords
        remove_words = [

            "open",
            "search",
            "website",
            "site",
            "khol",
            "khola",
            "gara",
            "gar"

        ]

        for word in remove_words:

            query = query.replace(word, "")

        query = query.strip()

        if not query:

            speak("Please say website name Gulshan.")
            return False

        # =====================================
        # SPECIAL WEBSITES
        # =====================================

        special_sites = {

            "youtube": "https://www.youtube.com",
            "facebook": "https://www.facebook.com",
            "fb": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "gmail": "https://mail.google.com",
            "email": "https://mail.google.com",
            "chatgpt": "https://chat.openai.com",
            "google": "https://www.google.com",
            "github": "https://github.com"

        }

        if query in special_sites:

            url = special_sites[query]

        # =====================================
        # SINGLE WORD = DIRECT WEBSITE
        # =====================================

        elif len(query.split()) == 1:

            domain = query.replace(" ", "")

            url = f"https://www.{domain}.com"

        # =====================================
        # MULTIPLE WORDS = GOOGLE SEARCH
        # =====================================

        else:

            encoded_query = urllib.parse.quote(query)

            url = (
                f"https://www.google.com/search?q={encoded_query}"
            )

        # =====================================
        # OPEN WEBSITE
        # =====================================

        speak("Just a moment Gulshan.")

        time.sleep(0.5)

        webbrowser.open(url)

        # memory
        opened_tabs.append(query)

        last_opened_tab = query

        smart_reply(
            OPENING_RESPONSES,
            query
        )

        return True

    except Exception as e:

        print(e)

        smart_reply(ERROR_RESPONSES)

        return False

# =====================================
# SMART TAB CLOSE
# =====================================

def smart_close_website(command):
    """
    Close browser tab
    """

    try:

        query = command.lower().strip()

        pyautogui.hotkey('ctrl', 'w')

        if query:

            smart_reply(
                CLOSING_RESPONSES,
                query
            )

        else:

            smart_reply(
                CLOSING_RESPONSES,
                "current tab"
            )

        return True

    except Exception as e:

        print(e)

        speak("Unable to close tab Gulshan.")

        return False

# =====================================
# CLOSE CURRENT WINDOW
# =====================================

def close_current_window():
    """
    Close active window
    """

    try:

        pyautogui.hotkey('alt', 'f4')

        smart_reply(
            CLOSING_RESPONSES,
            "window"
        )

        return True

    except Exception as e:

        print(e)

        speak("Unable to close window.")

        return False

# =====================================
# YOUTUBE FUNCTIONS
# =====================================

def youtube_open():

    webbrowser.open(
        "https://www.youtube.com"
    )

    smart_reply(
        OPENING_RESPONSES,
        "YouTube"
    )

def youtube_play_nepali(song_name=""):

    if song_name:

        query = f"{song_name} nepali song"

    else:

        nepali_songs = [

            "Resham Firiri",
            "Mutu Bhanda Mitho",
            "Samhalinchu",
            "Saili"

        ]

        query = random.choice(nepali_songs)

    webbrowser.open(

        f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"

    )

    speak(f"Okay Gulshan, playing {query}")

def youtube_play_bollywood(song_name=""):

    if song_name:

        query = f"{song_name} bollywood song"

    else:

        bollywood_songs = [

            "Kesariya",
            "Tum Hi Ho",
            "Kalank",
            "Channa Mereya"

        ]

        query = random.choice(bollywood_songs)

    webbrowser.open(

        f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"

    )

    speak(f"Playing {query} for you Gulshan")

def youtube_play_artist(artist_name):

    query = f"{artist_name} songs"

    webbrowser.open(

        f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"

    )

    speak(f"Playing {artist_name} songs Gulshan")

def youtube_play_song(song_name):

    webbrowser.open(

        f"https://www.youtube.com/results?search_query={urllib.parse.quote(song_name)}"

    )

    speak(f"Okay Gulshan, playing {song_name}")

# =====================================
# VIDEO CONTROLS
# =====================================

def youtube_pause():

    pyautogui.press('space')

    speak("Video paused Gulshan")

def youtube_resume():

    pyautogui.press('space')

    speak("Video resumed Gulshan")

def youtube_next():

    pyautogui.hotkey('shift', 'n')

    speak("Playing next video Gulshan")

def youtube_previous():

    pyautogui.hotkey('shift', 'p')

    speak("Playing previous video Gulshan")

def youtube_volume_up():

    for _ in range(3):

        pyautogui.press('up')

    speak("Volume increased Gulshan")

def youtube_volume_down():

    for _ in range(3):

        pyautogui.press('down')

    speak("Volume decreased Gulshan")

def youtube_fullscreen():

    pyautogui.press('f')

    speak("Fullscreen enabled Gulshan")

# =====================================
# WEBSITE SHORTCUTS
# =====================================

def open_google():

    webbrowser.open(
        "https://www.google.com"
    )

    smart_reply(
        OPENING_RESPONSES,
        "Google"
    )

def open_chatgpt():

    webbrowser.open(
        "https://chat.openai.com"
    )

    smart_reply(
        OPENING_RESPONSES,
        "ChatGPT"
    )

def open_facebook():

    webbrowser.open(
        "https://facebook.com"
    )

    smart_reply(
        OPENING_RESPONSES,
        "Facebook"
    )

def open_instagram():

    webbrowser.open(
        "https://instagram.com"
    )

    smart_reply(
        OPENING_RESPONSES,
        "Instagram"
    )

def open_gmail():

    webbrowser.open(
        "https://mail.google.com"
    )

    smart_reply(
        OPENING_RESPONSES,
        "Gmail"
    )

# =====================================
# TIME FUNCTIONS
# =====================================

def tell_time():

    now = datetime.datetime.now()

    current_time = now.strftime("%I:%M %p")

    speak(f"Gulshan, अहिले समय {current_time} भएको छ")

def tell_date():

    now = datetime.datetime.now()

    current_date = now.strftime(
        "%A, %B %d, %Y"
    )

    speak(f"Today is {current_date}")

# =====================================
# SCREENSHOT
# =====================================

def take_screenshot():

    timestamp = datetime.datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = f"screenshot_{timestamp}.png"

    try:

        screenshot = pyautogui.screenshot()

        screenshot.save(filename)

        speak(f"Screenshot saved as {filename}")

    except Exception as e:

        print(e)

        speak("Unable to take screenshot")

# =====================================
# SYSTEM CONTROLS
# =====================================

def shutdown_pc():

    speak(
        "Okay Gulshan, shutting down your computer in 5 seconds"
    )

    os.system("shutdown /s /t 5")

def restart_pc():

    speak(
        "Restarting your computer in 5 seconds Gulshan"
    )

    os.system("shutdown /r /t 5")

def lock_pc():

    speak("Locking your computer Gulshan")

    os.system(
        "rundll32.exe user32.dll,LockWorkStation"
    )

# =====================================
# CONVERSATION FUNCTIONS
# =====================================

def thank_you():

    responses = [

        "You're welcome Gulshan",

        "Happy to help Gulshan",

        "Anytime Gulshan",

        "My pleasure Gulshan",

        "सधैं तपाईंको सेवामा Gulshan"

    ]

    speak(random.choice(responses))

def how_are_you():

    responses = [

        "I am doing great Gulshan",

        "All systems operational Gulshan",

        "I am perfect and ready to help",

        "Everything is running smoothly Gulshan"

    ]

    speak(random.choice(responses))

def tell_joke():

    jokes = [

        "Why do programmers prefer dark mode? Because light attracts bugs.",

        "Why did the computer get cold? Because it left its windows open.",

        "Why was the laptop tired? Too many tabs open."

    ]

    speak(random.choice(jokes))

def introduce():

    intro = """

    Hello Gulshan.
    I am MJ, your personal AI assistant.

    I can open websites,
    search the internet,
    play YouTube videos,
    control your computer,
    take screenshots,
    and much more.

    How can I help you today?

    """

    speak(intro)

def show_help():

    help_text = """

    Here are some commands:

    - open facebook
    - youtube open
    - open nepali news
    - search AI tools

    - close it
    - close current tab
    - close window

    - play song
    - nepali song
    - bollywood song

    - pause
    - next
    - volume up

    - screenshot
    - time
    - help

    """

    speak(help_text)