from assistant.voice import listen
from assistant.actions import (
    speak,
    open_youtube,
    play_music,
    tell_time,
    search_google,
    shutdown_pc,
    restart_pc
)
from assistant.utils import get_activation_response

def run_brain(log, update_activation, close_callback):
    """Main brain with activation and close commands"""
    
    log("🔄 Initializing voice module...", "system")
    activated = False
    
    # All close command variations
    close_phrases = [
        "okay close it mj", "ok close it mj", "okay close mj",
        "mj close it", "close it mj", "mj close", "close mj",
        "close it", "close window", "close tab", "exit mj", "quit mj"
    ]
    
    while True:
        command = listen()
        
        if not command:
            continue
        
        log(f"🎤 Input: {command}", "command")
        
        # Activation
        if not activated and ("hey mj" in command or "mj" in command):
            response = get_activation_response()
            speak(response)
            log(f"🤖 {response}", "success")
            activated = True
            update_activation(True)
            continue
        
        if not activated:
            log("⏳ Say 'hey mj' to activate", "system")
            continue
        
        # Close commands
        if any(phrase in command for phrase in close_phrases):
            log("❌ Executing close command", "close")
            speak("Okay Gulshan, closing")
            close_callback()
            continue
        
        # Regular commands
        if "youtube" in command:
            log("▶ Opening YouTube...", "success")
            speak("Opening YouTube")
            open_youtube()
        
        elif "music" in command or "song" in command:
            log("▶ Playing music...", "success")
            speak("Playing music")
            play_music()
        
        elif "time" in command:
            log("⏰ Getting current time...", "success")
            tell_time()
        
        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                log(f"🔍 Searching: {query}", "success")
                speak(f"Searching for {query}")
                search_google(query)
            else:
                log("❓ What should I search for?", "error")
                speak("What should I search for?")
        
        elif "shutdown" in command:
            log("🔴 Shutting down PC...", "close")
            speak("Shutting down")
            shutdown_pc()
        
        elif "restart" in command:
            log("🔄 Restarting PC...", "close")
            speak("Restarting")
            restart_pc()
        
        elif "deactivate" in command or "sleep" in command:
            log("💤 Deactivating...", "system")
            speak("Going to sleep")
            activated = False
            update_activation(False)
        
        elif "exit" in command or "quit" in command:
            log("👋 Goodbye!", "close")
            speak("Goodbye Gulshan")
            break
        
        else:
            log("❌ Command not recognized", "error")
            speak("I don't know that command")