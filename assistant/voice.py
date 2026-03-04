import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

recognizer = sr.Recognizer()

def speak(text):
    print("MJ:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Could not request results; check your internet connection.")
        return ""