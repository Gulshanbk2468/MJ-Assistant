"""
MJ ASSISTANT - BRAIN MODULE
FINAL VERSION - SMART WEBSITE CONTROL + ALL FEATURES
"""

from assistant.voice import listen
from assistant.actions import *

from assistant.utils import (
    get_activation_response,
    get_error_response
)

import time


# =====================================
# MAIN BRAIN
# =====================================

def run_brain(log, update_activation, close_callback):
    """
    Main MJ Brain
    """

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

            activation_words = [

                "hey mj",
                "mj",
                "hey",
                "em jay",
                "m j",
                "mj assistant"

            ]

            if not activated:

                if any(
                    word in command_lower
                    for word in activation_words
                ):

                    response = get_activation_response()

                    speak(response)

                    log(f"🤖 {response}", "success")

                    activated = True

                    update_activation(True)

                else:

                    log(
                        "⏳ Say 'hey mj' to activate",
                        "system"
                    )

                continue

            # =====================================
            # EXIT / DEACTIVATE
            # =====================================

            if any(x in command_lower for x in [

                "sleep mj",
                "go sleep",
                "deactivate",
                "stop listening"

            ]):

                speak("Going to sleep")

                log("💤 MJ deactivated", "close")

                activated = False

                update_activation(False)

                continue

            # =====================================
            # SMART WEBSITE OPEN
            # =====================================

            open_words = [

                "open",
                "search",
                "khol",
                "khola"

            ]

            if any(word in command_lower for word in open_words):

                query = command_lower

                # remove keywords
                for word in open_words:

                    query = query.replace(word, "")

                query = query.strip()

                if query:

                    log(
                        f"🌐 Opening {query}...",
                        "success"
                    )

                    smart_open_website(query)

                    continue

            # =====================================
            # SMART WEBSITE CLOSE
            # =====================================

            close_words = [

                "close",
                "banda",
                "band"

            ]

            if any(word in command_lower for word in close_words):

                # current tab
                if any(x in command_lower for x in [

                    "it",
                    "this",
                    "current",
                    "tab",
                    "window"

                ]):

                    log(
                        "❌ Closing current tab...",
                        "close"
                    )

                    smart_close_website(
                        command_lower
                    )

                    continue

                # specific close
                else:

                    query = command_lower

                    for word in close_words:

                        query = query.replace(
                            word,
                            ""
                        )

                    query = query.strip()

                    if query:

                        log(
                            f"❌ Closing {query}...",
                            "close"
                        )

                        smart_close_website(
                            query
                        )

                        continue

            # =====================================
            # YOUTUBE SONG PLAY
            # =====================================

            if "play" in command_lower:

                song = (
                    command_lower
                    .replace("play", "")
                    .replace("song", "")
                    .strip()
                )

                if song:

                    log(
                        f"🎵 Playing {song}...",
                        "success"
                    )

                    youtube_play_song(song)

                    continue

            # =====================================
            # NEPALI SONG
            # =====================================

            if any(x in command_lower for x in [

                "nepali song",
                "नेपाली गीत"

            ]):

                log(
                    "🎵 Playing Nepali songs...",
                    "success"
                )

                youtube_play_nepali()

                continue

            # =====================================
            # BOLLYWOOD SONG
            # =====================================

            if any(x in command_lower for x in [

                "bollywood song",
                "hindi song",
                "बलिउड गीत"

            ]):

                log(
                    "🎵 Playing Bollywood songs...",
                    "success"
                )

                youtube_play_bollywood()

                continue

            # =====================================
            # ARTISTS
            # =====================================

            if "arijit singh" in command_lower:

                log(
                    "🎵 Playing Arijit Singh...",
                    "success"
                )

                youtube_play_artist(
                    "arijit singh"
                )

                continue

            if "atif aslam" in command_lower:

                log(
                    "🎵 Playing Atif Aslam...",
                    "success"
                )

                youtube_play_artist(
                    "atif aslam"
                )

                continue

            if "nepathya" in command_lower:

                log(
                    "🎵 Playing Nepathya...",
                    "success"
                )

                youtube_play_artist(
                    "nepathya"
                )

                continue

            # =====================================
            # VIDEO CONTROLS
            # =====================================

            if any(x in command_lower for x in [

                "pause",
                "rok"

            ]):

                log("⏸️ Pausing...", "success")

                youtube_pause()

                continue

            if any(x in command_lower for x in [

                "resume",
                "play again"

            ]):

                log("▶️ Resuming...", "success")

                youtube_resume()

                continue

            if any(x in command_lower for x in [

                "next",
                "arko"

            ]):

                log("⏭️ Next video...", "success")

                youtube_next()

                continue

            if any(x in command_lower for x in [

                "previous",
                "pahilo"

            ]):

                log("⏮️ Previous video...", "success")

                youtube_previous()

                continue

            if any(x in command_lower for x in [

                "volume up",
                "awaz badha"

            ]):

                log("🔊 Volume up...", "success")

                youtube_volume_up()

                continue

            if any(x in command_lower for x in [

                "volume down",
                "awaz kam"

            ]):

                log("🔉 Volume down...", "success")

                youtube_volume_down()

                continue

            if any(x in command_lower for x in [

                "fullscreen",
                "full screen"

            ]):

                log("🖥️ Fullscreen...", "success")

                youtube_fullscreen()

                continue

            # =====================================
            # TIME
            # =====================================

            if any(x in command_lower for x in [

                "time",
                "समय"

            ]):

                log("⏰ Getting time...", "success")

                tell_time()

                continue

            # =====================================
            # DATE
            # =====================================

            if any(x in command_lower for x in [

                "date",
                "मिति"

            ]):

                log("📅 Getting date...", "success")

                tell_date()

                continue

            # =====================================
            # SCREENSHOT
            # =====================================

            if any(x in command_lower for x in [

                "screenshot",
                "photo le"

            ]):

                log(
                    "📸 Taking screenshot...",
                    "success"
                )

                take_screenshot()

                continue

            # =====================================
            # SYSTEM CONTROLS
            # =====================================

            if "shutdown" in command_lower:

                log(
                    "🔴 Shutting down...",
                    "close"
                )

                shutdown_pc()

                continue

            if any(x in command_lower for x in [

                "restart",
                "reboot"

            ]):

                log(
                    "🔄 Restarting...",
                    "close"
                )

                restart_pc()

                continue

            if "lock" in command_lower:

                log(
                    "🔒 Locking PC...",
                    "close"
                )

                lock_pc()

                continue

            # =====================================
            # INTRODUCTION
            # =====================================

            if any(x in command_lower for x in [

                "who are you",
                "introduce"

            ]):

                log(
                    "🤖 Introducing MJ...",
                    "success"
                )

                introduce()

                continue

            # =====================================
            # HELP
            # =====================================

            if any(x in command_lower for x in [

                "help",
                "commands"

            ]):

                log(
                    "📚 Showing help...",
                    "success"
                )

                show_help()

                continue

            # =====================================
            # THANK YOU
            # =====================================

            if any(x in command_lower for x in [

                "thank",
                "thanks",
                "धन्यवाद"

            ]):

                thank_you()

                continue

            # =====================================
            # HOW ARE YOU
            # =====================================

            if any(x in command_lower for x in [

                "how are you",
                "kata chhau"

            ]):

                how_are_you()

                continue

            # =====================================
            # JOKE
            # =====================================

            if any(x in command_lower for x in [

                "joke",
                "मजाक"

            ]):

                tell_joke()

                continue

            # =====================================
            # UNKNOWN COMMAND
            # =====================================

            error_msg = get_error_response()

            speak(error_msg)

            log(
                "❌ Command not recognized",
                "error"
            )

        except Exception as e:

            log(
                f"⚠️ Error: {str(e)}",
                "error"
            )

            time.sleep(0.5)

            continue