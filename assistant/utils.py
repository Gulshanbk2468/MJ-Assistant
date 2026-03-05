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
    """Professional greeting based on Nepali time"""
    now = get_nepali_time()
    hour = now.hour
    
    # Time-based greeting
    if 5 <= hour < 12:
        time_greeting = "Good morning"
        time_emoji = "🌅"
    elif 12 <= hour < 17:
        time_greeting = "Good afternoon"
        time_emoji = "☀️"
    elif 17 <= hour < 20:
        time_greeting = "Good evening"
        time_emoji = "🌆"
    else:
        time_greeting = "Good night"
        time_emoji = "🌙"
    
    # Professional greeting variations
    greetings = [
        f"{time_emoji} {time_greeting} {USER_NAME}. MJ system online and ready.",
        f"{time_emoji} Welcome back {USER_NAME}. MJ is fully operational.",
        f"{time_emoji} {time_greeting} {USER_NAME}. All systems running smoothly.",
        f"{time_emoji} System active. {time_greeting} {USER_NAME}. MJ at your service.",
        f"{time_emoji} {USER_NAME}, MJ initialized. Ready for your commands."
    ]
    
    return random.choice(greetings)

def get_activation_response():
    """Response when user says 'Hey MJ'"""
    responses = [
        f"Yes {USER_NAME}, I'm listening. 🎤",
        f"Ready {USER_NAME}. What can I do for you? ⚡",
        f"Listening {USER_NAME}. Go ahead. 🎯",
        f"At your service {USER_NAME}. What's your command? 💫",
        f"MJ active. Waiting for your instruction {USER_NAME}. 🔥"
    ]
    return random.choice(responses)

def get_command_response(command):
    """Response after executing a command"""
    responses = [
        f"Done {USER_NAME}! ✅",
        f"Completed {USER_NAME}. ⚡",
        f"Task executed {USER_NAME}. 🎯",
        f"All set {USER_NAME}! 🔥"
    ]
    return random.choice(responses)