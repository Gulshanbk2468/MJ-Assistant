"""
MJ ASSISTANT - UTILS MODULE
"""

import random
import datetime
import pytz

USER_NAME = "Gulshan"

def get_nepali_time():
    """Get current Nepali time"""
    try:
        nepali_tz = pytz.timezone('Asia/Kathmandu')
        return datetime.datetime.now(nepali_tz)
    except:
        return datetime.datetime.now()

def get_greeting():
    """Get greeting message"""
    now = get_nepali_time()
    hour = now.hour
    
    if hour < 12:
        time_greeting = "Good morning"
        emoji = "🌅"
    elif hour < 17:
        time_greeting = "Good afternoon"
        emoji = "☀️"
    else:
        time_greeting = "Good evening"
        emoji = "🌆"
    
    greetings = [
        f"{emoji} {time_greeting} {USER_NAME}. MJ system online and ready.",
        f"{emoji} Welcome back {USER_NAME}. MJ is fully operational.",
        f"{emoji} {time_greeting} {USER_NAME}. All systems running smoothly.",
        f"{emoji} {USER_NAME}, MJ initialized. Ready for your commands."
    ]
    
    return random.choice(greetings)

def get_activation_response():
    """Response when user says 'hey MJ'"""
    responses = [
        f"Yes {USER_NAME}, I'm listening. 🎤",
        f"Ready {USER_NAME}. What can I do for you? ⚡",
        f"Listening {USER_NAME}. Go ahead. 🎯",
        f"At your service {USER_NAME}. What's your command? 💫",
        f"MJ active. Waiting for your instruction {USER_NAME}. 🔥"
    ]
    return random.choice(responses)