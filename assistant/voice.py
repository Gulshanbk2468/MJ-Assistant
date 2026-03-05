import speech_recognition as sr


recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("Listening...")

        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            return command.lower()

        except:
            return ""