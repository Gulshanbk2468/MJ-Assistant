from assistant.voice import speak, listen
from assistant.actions import execute

def run():
    speak("MJ system ready. Say hey MJ to activate.")

    while True:
        command = listen()

        if command == "":
            continue

        # Activation word
        if "hey mj" in command:
            speak("Yes Gulshan, I am listening.")
            continue

        result = execute(command)

        if result == "exit":
            break