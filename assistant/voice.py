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

recognizer.energy_threshold = 3000
recognizer.dynamic_energy_threshold = True

recognizer.pause_threshold = 0.8
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

    # common replacements
    replacements = {

        "fb": "facebook",

        "insta": "instagram",

        "mail": "gmail",

        "you tube": "youtube",

        "chat gpt": "chatgpt",

        "एमजे": "mj",
    }

    for old, new in replacements.items():

        command = command.replace(old, new)

    return command