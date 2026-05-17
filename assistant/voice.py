"""
MJ ASSISTANT - VOICE MODULE
FINAL VERSION - Nepali + English + Hindi
"""

import speech_recognition as sr
import time


# =====================================
# RECOGNIZER SETUP
# =====================================

recognizer = sr.Recognizer()

recognizer.energy_threshold = 1200
recognizer.dynamic_energy_threshold = True

recognizer.pause_threshold = 1.0
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5

# =====================================
# LISTEN FUNCTION
# =====================================

def listen():
    """
    Listen for voice command
    """

    try:

        with sr.Microphone() as source:

            print("🎤 Listening...")

            # noise adjustment
            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            try:

                # listen
                audio = recognizer.listen(
                    source,
                    timeout=3,
                    phrase_time_limit=5
                )

                print("⚡ Processing voice...")

                # =====================================
                # ENGLISH
                # =====================================

                try:

                    command = recognizer.recognize_google(
                        audio,
                        language='en-US'
                    )

                    print(f"✅ You said (EN): {command}")

                    return clean_command(command)

                except:

                    pass

                # =====================================
                # NEPALI
                # =====================================

                try:

                    command = recognizer.recognize_google(
                        audio,
                        language='ne-NP'
                    )

                    print(f"✅ You said (NP): {command}")

                    return clean_command(command)

                except:

                    pass

                # =====================================
                # HINDI
                # =====================================

                try:

                    command = recognizer.recognize_google(
                        audio,
                        language='hi-IN'
                    )

                    print(f"✅ You said (HI): {command}")

                    return clean_command(command)

                except:

                    pass

                return ""

            except sr.WaitTimeoutError:

                return ""

            except Exception as e:

                print(f"⚠️ Voice processing error: {e}")

                return ""

    except Exception as e:

        print(f"⚠️ Microphone error: {e}")

        return ""


# =====================================
# CLEAN COMMAND
# =====================================

def clean_command(command):
    """
    Clean voice command
    """

    command = command.lower().strip()

    # remove unwanted spaces
    command = " ".join(command.split())

    # =====================================
    # COMMON REPLACEMENTS
    # =====================================

    replacements = {

        # apps
        "fb": "facebook",
        "face book": "facebook",

        "insta": "instagram",

        "mail": "gmail",
        "e mail": "gmail",

        "you tube": "youtube",

        "chat gpt": "chatgpt",

        # assistant name
        "एमजे": "mj",

        # open words
        "खोल": "open",
        "खोल्नु": "open",
        "खोल्नुस": "open",
        "खोल्न": "open",

        "khol": "open",
        "khola": "open",

        # close words
        "बन्द": "close",
        "बंद": "close",

        "banda": "close",
        "band": "close",

        # misc
        "current tab": "current",
        "this tab": "current",
    }

    for old, new in replacements.items():

        command = command.replace(old, new)

    # =====================================
    # REMOVE EXTRA WORDS
    # =====================================

    remove_words = [

        "gar",
        "gara",
        "please",
        "jara",
        "zara",
        "mj",
    ]

    for word in remove_words:

        command = command.replace(word, "")

    # clean again
    command = " ".join(command.split())

    print(f"🧠 Cleaned Command: {command}")

    return command