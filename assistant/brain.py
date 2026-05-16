"""
MJ ASSISTANT - BRAIN MODULE
FINAL VERSION - All functions working with voice
"""

from assistant.voice import listen
from assistant.actions import *
from assistant.utils import get_activation_response, get_error_response
import time

def run_brain(log, update_activation, close_callback):
    """Main brain with all functions working"""
    
    log("🔄 MJ system initializing...", "system")
    activated = False
    
    while True:
        try:
            command = listen()
            
            if not command or command == "":
                time.sleep(0.1)
                continue
            
            command_lower = command.lower().strip()
            log(f"🎤 You said: {command_lower}", "command")
            
            # =====================================
            # ACTIVATION
            # =====================================
            if not activated:
                if 'hey mj' in command_lower or 'mj' in command_lower:
                    response = get_activation_response()
                    speak(response)
                    log(f"🤖 {response}", "success")
                    activated = True
                    update_activation(True)
                else:
                    log("⏳ Say 'hey mj' to activate", "system")
                continue
            
            # =====================================
            # CLOSE WINDOW
            # =====================================
            if any(x in command_lower for x in ['close it', 'band gara', 'close window', 'window close', 'close mj']):
                log("🪟 Closing window...", "close")
                close_current_window()
                continue
            
            # =====================================
            # YOUTUBE OPEN
            # =====================================
            if any(x in command_lower for x in ['open youtube', 'youtube khol', 'youtube open', 'yt khol']):
                log("▶️ Opening YouTube...", "success")
                youtube_open()
                continue
            
            # =====================================
            # NEPALI SONG
            # =====================================
            if any(x in command_lower for x in ['nepali song', 'नेपाली गीत']):
                log("🎵 Playing Nepali song...", "success")
                youtube_play_nepali()
                continue
            
            # =====================================
            # BOLLYWOOD SONG
            # =====================================
            if any(x in command_lower for x in ['bollywood song', 'बलिउड गीत', 'hindi song']):
                log("🎵 Playing Bollywood song...", "success")
                youtube_play_bollywood()
                continue
            
            # =====================================
            # ARTIST SONGS
            # =====================================
            if 'arijit singh' in command_lower:
                log("🎵 Playing Arijit Singh songs...", "success")
                youtube_play_artist('arijit singh')
                continue
                
            if 'atif aslam' in command_lower:
                log("🎵 Playing Atif Aslam songs...", "success")
                youtube_play_artist('atif aslam')
                continue
                
            if 'nepathya' in command_lower:
                log("🎵 Playing Nepathya songs...", "success")
                youtube_play_artist('nepathya')
                continue
            
            # =====================================
            # PLAY SPECIFIC SONG
            # =====================================
            if 'play' in command_lower:
                song = command_lower.replace('play', '').replace('song', '').strip()
                if song:
                    log(f"🎵 Playing {song}...", "success")
                    youtube_play_song(song)
                continue
            
            # =====================================
            # VIDEO CONTROL
            # =====================================
            if any(x in command_lower for x in ['pause', 'rok', 'रोक']):
                log("⏸️ Pausing video...", "success")
                youtube_pause()
                continue
                
            if any(x in command_lower for x in ['resume', 'feri chalau', 'play again']):
                log("▶️ Resuming video...", "success")
                youtube_resume()
                continue
                
            if any(x in command_lower for x in ['next', 'arko', 'अर्को']):
                log("⏭️ Next video...", "success")
                youtube_next()
                continue
                
            if any(x in command_lower for x in ['previous', 'pahilo', 'पहिलो']):
                log("⏮️ Previous video...", "success")
                youtube_previous()
                continue
                
            if any(x in command_lower for x in ['volume up', 'awaz badha', 'आवाज बढाउ']):
                log("🔊 Volume up...", "success")
                youtube_volume_up()
                continue
                
            if any(x in command_lower for x in ['volume down', 'awaz kam', 'आवाज घटाउ']):
                log("🔉 Volume down...", "success")
                youtube_volume_down()
                continue
                
            if any(x in command_lower for x in ['fullscreen', 'pura screen']):
                log("🖥️ Fullscreen...", "success")
                youtube_fullscreen()
                continue
            
            # =====================================
            # WEBSITES
            # =====================================
            if any(x in command_lower for x in ['google khol', 'google open']):
                log("🌐 Opening Google...", "success")
                open_google()
                continue
                
            if any(x in command_lower for x in ['chatgpt khol', 'chat gpt']):
                log("🤖 Opening ChatGPT...", "success")
                open_chatgpt()
                continue
                
            if any(x in command_lower for x in ['facebook khol', 'fb khol']):
                log("📘 Opening Facebook...", "success")
                open_facebook()
                continue
                
            if any(x in command_lower for x in ['instagram khol', 'insta']):
                log("📷 Opening Instagram...", "success")
                open_instagram()
                continue
                
            if any(x in command_lower for x in ['gmail khol', 'mail']):
                log("📧 Opening Gmail...", "success")
                open_gmail()
                continue
            
            # =====================================
            # TIME & DATE
            # =====================================
            if any(x in command_lower for x in ['time kati', 'what time', 'समय']):
                log("⏰ Getting time...", "success")
                tell_time()
                continue
                
            if any(x in command_lower for x in ['date kati', 'what date', 'मिति']):
                log("📅 Getting date...", "success")
                tell_date()
                continue
            
            # =====================================
            # SYSTEM
            # =====================================
            if any(x in command_lower for x in ['screenshot', 'photo le', 'स्क्रिनसट']):
                log("📸 Taking screenshot...", "success")
                take_screenshot()
                continue
                
            if any(x in command_lower for x in ['shutdown', 'band gara']):
                log("🔴 Shutting down...", "close")
                shutdown_pc()
                continue
                
            if any(x in command_lower for x in ['restart', 'reboot']):
                log("🔄 Restarting...", "close")
                restart_pc()
                continue
                
            if any(x in command_lower for x in ['lock', 'लक']):
                log("🔒 Locking PC...", "close")
                lock_pc()
                continue
            
            # =====================================
            # INTRO
            # =====================================
            if any(x in command_lower for x in ['who are you', 'timí ko ho', 'introduce']):
                log("🤖 Introducing MJ...", "success")
                introduce()
                continue
            
            # =====================================
            # HELP
            # =====================================
            if any(x in command_lower for x in ['help', 'commands', 'सहायता']):
                log("📚 Showing help...", "success")
                show_help()
                continue
            
            # =====================================
            # CONVERSATION
            # =====================================
            if any(x in command_lower for x in ['thank', 'thanks', 'धन्यवाद']):
                thank_you()
                continue
                
            if any(x in command_lower for x in ['how are you', 'kata chhau']):
                how_are_you()
                continue
                
            if any(x in command_lower for x in ['joke', 'मजाक']):
                tell_joke()
                continue
            
            # =====================================
            # NOT RECOGNIZED
            # =====================================
            error_msg = get_error_response()
            speak(error_msg)
            log(f"❌ Command not recognized", "error")
            
        except Exception as e:
            log(f"⚠️ Error: {str(e)}", "error")
            time.sleep(0.5)
            continue