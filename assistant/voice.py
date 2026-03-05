import speech_recognition as sr
import time

recognizer = sr.Recognizer()

def listen():
    """Listen for voice input and return text"""
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
                command = recognizer.recognize_google(audio)
                return command.lower()
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                print("⚠️ Internet connection error")
                return ""
            except Exception as e:
                print(f"⚠️ Error: {e}")
                return ""
    except Exception as e:
        print(f"⚠️ Microphone error: {e}")
        return ""   