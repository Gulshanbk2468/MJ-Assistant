"""
MJ ASSISTANT - VOICE MODULE
Fixed for Nepali + English recognition
"""

import speech_recognition as sr
import time

recognizer = sr.Recognizer()

# Optimize settings
recognizer.energy_threshold = 3000
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.phrase_threshold = 0.3
recognizer.non_speaking_duration = 0.5

def listen():
    """Listen for voice input with better accuracy"""
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                # Listen with timeout
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=4)
                print("🎤 Processing...")
                
                # Try multiple language recognitions
                try:
                    # First try English
                    command = recognizer.recognize_google(audio, language='en-US')
                    print(f"✅ You said (EN): {command}")
                    return command.lower()
                except:
                    try:
                        # Then try Nepali
                        command = recognizer.recognize_google(audio, language='ne-NP')
                        print(f"✅ You said (NP): {command}")
                        return command.lower()
                    except:
                        try:
                            # Finally try Hindi (similar to Nepali)
                            command = recognizer.recognize_google(audio, language='hi-IN')
                            print(f"✅ You said (HI): {command}")
                            return command.lower()
                        except:
                            return ""
                            
            except sr.WaitTimeoutError:
                return ""
            except Exception as e:
                return ""
                
    except Exception as e:
        print(f"⚠️ Microphone error: {e}")
        return ""