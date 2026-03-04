import webbrowser
import os
from assistant.voice import speak

def execute(command):

    # OPEN YOUTUBE
    if "open youtube" in command:
        speak("Okay Gulshan, opening YouTube.")
        webbrowser.open_new_tab("https://www.youtube.com")

    # OPEN GOOGLE
    elif "open google" in command:
        speak("Okay Gulshan, opening Google.")
        webbrowser.open_new_tab("https://www.google.com")

    # CLOSE CURRENT WINDOW (Windows shortcut)
    elif "close it" in command or "close window" in command:
        speak("Okay Gulshan, closing it.")
        os.system("taskkill /im chrome.exe /f")

    # EXIT PROGRAM
    elif "exit" in command or "shutdown mj" in command:
        speak("MJ shutting down. Goodbye Gulshan.")
        return "exit"

    else:
        speak("Sorry Gulshan, I don't know that command yet.")