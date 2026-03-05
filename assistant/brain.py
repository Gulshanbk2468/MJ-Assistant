"""
MJ ASSISTANT - BRAIN MODULE
"""

from assistant.voice import listen
from assistant.actions import *
from assistant.utils import get_greeting, get_activation_response
import time

def run_brain(log, update_activation, close_callback):
    """Main brain with all command patterns"""
    
    log("🔄 MJ system initializing...", "system")
    activated = False
    
    # Activation patterns
    activation_patterns = ['hey mj', 'mj', 'हे म्ज', 'म्ज']
    
    # Close patterns
    close_patterns = [
        'close it', 'band gara', 'close gara', 'window band',
        'close window', 'band de', 'yo band gara', 'close it mj',
        'band gara mj', 'close mj'
    ]
    
    while True:
        try:
            command = listen()
            
            if not command or command == "":
                time.sleep(0.1)
                continue
            
            command_lower = command.lower().strip()
            log(f"🎤 Input: {command_lower}", "command")
            
            # =====================================
            # ACTIVATION
            # =====================================
            if not activated:
                if any(pattern in command_lower for pattern in activation_patterns):
                    response = get_activation_response()
                    speak(response)
                    log(f"🤖 {response}", "success")
                    activated = True
                    update_activation(True)
                else:
                    log("⏳ Say 'hey mj' to activate", "system")
                continue
            
            # =====================================
            # CLOSE COMMANDS
            # =====================================
            if any(pattern in command_lower for pattern in close_patterns):
                log("❌ Closing window...", "close")
                speak("Window band garchhu")
                close_callback()
                continue
            
            # =====================================
            # YOUTUBE OPEN
            # =====================================
            if ('youtube' in command_lower or 'yt' in command_lower) and ('khol' in command_lower or 'open' in command_lower):
                if 'arko' in command_lower or 'new' in command_lower or 'another' in command_lower:
                    log("🆕 Opening new YouTube tab...", "success")
                    youtube_new_tab()
                else:
                    log("▶️ Opening YouTube...", "success")
                    youtube_open()
                continue
            
            # =====================================
            # YOUTUBE CLOSE
            # =====================================
            if ('youtube' in command_lower or 'yt' in command_lower) and ('band' in command_lower or 'close' in command_lower):
                log("❌ Closing YouTube tab...", "close")
                youtube_close_tab()
                continue
            
            # =====================================
            # YOUTUBE SEARCH
            # =====================================
            if ('youtube search' in command_lower or 'search in youtube' in command_lower or 'yt search' in command_lower):
                query = command_lower.replace('youtube search', '')
                query = query.replace('search in youtube', '')
                query = query.replace('yt search', '')
                query = query.replace('in youtube', '')
                query = query.replace('ma', '')
                query = query.replace('khoj', '')
                query = query.replace('mj', '').strip()
                
                if query:
                    log(f"🎵 Searching YouTube for: {query}", "success")
                    youtube_search(query)
                else:
                    speak("Ke khojnu chahanchha?")
                continue
            
            # =====================================
            # PLAY SONG
            # =====================================
            if 'play' in command_lower and ('song' in command_lower or 'youtube' in command_lower):
                query = command_lower.replace('play', '')
                query = query.replace('song', '')
                query = query.replace('youtube', '')
                query = query.replace('mj', '').strip()
                
                if query:
                    log(f"🎵 Playing on YouTube: {query}", "success")
                    youtube_search(query)
                else:
                    speak("Ke play garnu chahanchha?")
                continue
            
            # =====================================
            # VIDEO CONTROL
            # =====================================
            if 'pause' in command_lower or 'rok' in command_lower:
                youtube_pause()
                continue
            
            if 'resume' in command_lower or 'feri chalau' in command_lower:
                youtube_resume()
                continue
            
            if 'next video' in command_lower or 'arko video' in command_lower:
                youtube_next()
                continue
            
            if 'previous video' in command_lower or 'pahilo video' in command_lower:
                youtube_previous()
                continue
            
            if 'first video' in command_lower or 'pahilo video play' in command_lower:
                youtube_play_first()
                continue
            
            # =====================================
            # VOLUME CONTROL
            # =====================================
            if ('volume up' in command_lower or 'awaz badha' in command_lower):
                youtube_volume_up()
                continue
            
            if ('volume down' in command_lower or 'awaz kam' in command_lower):
                youtube_volume_down()
                continue
            
            # =====================================
            # TAB CONTROL
            # =====================================
            if ('next tab' in command_lower or 'arko tab' in command_lower):
                youtube_next_tab()
                continue
            
            if ('previous tab' in command_lower or 'pahilo tab' in command_lower):
                youtube_prev_tab()
                continue
            
            # =====================================
            # FULLSCREEN
            # =====================================
            if 'fullscreen' in command_lower or 'pura screen' in command_lower:
                youtube_fullscreen()
                continue
            
            # =====================================
            # WEBSITES
            # =====================================
            if 'google' in command_lower and ('khol' in command_lower or 'open' in command_lower):
                open_google()
                continue
            
            if 'chatgpt' in command_lower or 'chat gpt' in command_lower:
                open_chatgpt()
                continue
            
            if 'deepseek' in command_lower:
                open_deepseek()
                continue
            
            if 'github' in command_lower:
                open_github()
                continue
            
            if 'gmail' in command_lower:
                open_gmail()
                continue
            
            # =====================================
            # SEARCH
            # =====================================
            if 'search' in command_lower or 'khoj' in command_lower:
                if 'youtube' not in command_lower:
                    query = command_lower.replace('search', '')
                    query = query.replace('khoj', '')
                    query = query.replace('google', '')
                    query = query.replace('mj', '').strip()
                    
                    if query:
                        log(f"🔍 Searching Google for: {query}", "success")
                        search_google(query)
                    else:
                        speak("Ke khojnu chahanchha?")
                continue
            
            # =====================================
            # TIME
            # =====================================
            if 'time' in command_lower or 'समय' in command_lower or 'kati bhayo' in command_lower:
                tell_time()
                continue
            
            if 'date' in command_lower or 'मिति' in command_lower:
                tell_date()
                continue
            
            # =====================================
            # SYSTEM
            # =====================================
            if 'shutdown' in command_lower or 'band gara' in command_lower:
                shutdown_pc()
                continue
            
            if 'restart' in command_lower:
                restart_pc()
                continue
            
            if 'lock' in command_lower:
                lock_pc()
                continue
            
            # =====================================
            # APPS
            # =====================================
            if 'notepad' in command_lower:
                open_notepad()
                continue
            
            if 'calculator' in command_lower:
                open_calculator()
                continue
            
            if 'cmd' in command_lower or 'command prompt' in command_lower:
                open_cmd()
                continue
            
            # =====================================
            # SCREENSHOT
            # =====================================
            if 'screenshot' in command_lower or 'photo le' in command_lower:
                take_screenshot()
                continue
            
            # =====================================
            # CONVERSATION
            # =====================================
            if 'thank' in command_lower or 'thanks' in command_lower:
                thank_you()
                continue
            
            if 'how are you' in command_lower:
                how_are_you()
                continue
            
            if 'joke' in command_lower:
                tell_joke()
                continue
            
            if 'who are you' in command_lower:
                introduce()
                continue
            
            if 'help' in command_lower:
                show_help()
                continue
            
            # =====================================
            # NOT RECOGNIZED
            # =====================================
            log("❌ Command not recognized", "error")
            speak("Maile bujhina. Pheri bhanu na.")
            
        except Exception as e:
            log(f"⚠️ Error: {str(e)}", "error")
            time.sleep(0.5)
            continue