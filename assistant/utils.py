import random
import datetime

USER_NAME = "Gulshan"

def get_greeting():

    hour = datetime.datetime.now().hour

    if hour < 12:
        base = "Good morning"
    elif hour < 18:
        base = "Good afternoon"
    else:
        base = "Good evening"

    greetings = [
        f"{base} {USER_NAME}. Jarvix online. How may I assist you?",
        f"Welcome back {USER_NAME}. All systems operational.",
        f"{base} {USER_NAME}. I'm ready for your command.",
        f"{USER_NAME}, Jarvix activated. Awaiting instructions."
    ]

    return random.choice(greetings)
