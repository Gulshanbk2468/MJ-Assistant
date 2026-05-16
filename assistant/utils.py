"""
MJ ASSISTANT - UTILS MODULE
Premium version with Nepali time and natural responses
"""

import random
import datetime
import pytz

USER_NAME = "Gulshan"

def get_nepali_time():
    """Get current Nepali time (Nepal Standard Time = UTC+5:45)"""
    try:
        nepali_tz = pytz.timezone('Asia/Kathmandu')
        return datetime.datetime.now(nepali_tz)
    except:
        return datetime.datetime.now()

def get_greeting():
    """Get personalized greeting based on Nepali time"""
    now = get_nepali_time()
    hour = now.hour
    
    # Time-based greeting in Nepali style
    if 4 <= hour < 12:
        time_greeting = "शुभ प्रभात"  # Good morning
        emoji = "🌅"
        eng_greeting = "Good morning"
    elif 12 <= hour < 17:
        time_greeting = "शुभ दिउँसो"  # Good afternoon
        emoji = "☀️"
        eng_greeting = "Good afternoon"
    elif 17 <= hour < 20:
        time_greeting = "शुभ सन्ध्या"  # Good evening
        emoji = "🌆"
        eng_greeting = "Good evening"
    else:
        time_greeting = "शुभ रात्री"  # Good night
        emoji = "🌙"
        eng_greeting = "Good night"
    
    # Premium greeting variations
    greetings = [
        f"{emoji} {time_greeting} {USER_NAME}! MJ system activated. How may I assist you today?",
        f"{emoji} {eng_greeting} {USER_NAME}! MJ is ready and waiting for your command.",
        f"{emoji} नमस्ते {USER_NAME}! MJ तपाईंको सेवामा तयार छ।",
        f"{emoji} Welcome back {USER_NAME}! MJ is fully operational. What can I do for you?",
        f"{emoji} {time_greeting} {USER_NAME}! All systems online. I'm here to help."
    ]
    
    return random.choice(greetings)

def get_activation_response():
    """Response when user says 'hey MJ'"""
    responses = [
        f"Yes {USER_NAME}? I'm listening. 🎤",
        f"Ready {USER_NAME}. What can I do for you? ⚡",
        f"Listening {USER_NAME}. Go ahead. 🎯",
        f"At your service {USER_NAME}. What's your command? 💫",
        f"MJ active. Waiting for your instruction {USER_NAME}. 🔥",
        f"जी हजुर {USER_NAME}! के सहयोग गर्न सक्छु?",
        f"हजुर {USER_NAME}! के काम छ?"
    ]
    return random.choice(responses)

# =====================================
# 🔥 NEW FUNCTIONS ADDED HERE
# =====================================

def get_thank_you_response():
    """Response when user says thank you"""
    responses = [
        f"You're welcome {USER_NAME}! 😊",
        f"Happy to help {USER_NAME}! 🙏",
        f"Anytime {USER_NAME}! That's what I'm here for. 💫",
        f"तपाईंलाई सधैं सहयोग गर्न पाउँदा खुशी {USER_NAME}!",
        f"Kehi chaincha bhane pheri bhanu hai {USER_NAME}! ✨",
        f"Welcome {USER_NAME}! Let me know if you need anything else.",
        f"My pleasure {USER_NAME}! Always happy to assist."
    ]
    return random.choice(responses)

def get_command_complete_response(command=""):
    """Response after completing a command"""
    responses = [
        f"Done {USER_NAME}! ✅",
        f"Command executed {USER_NAME}! ⚡",
        f"Task completed {USER_NAME}! ✨",
        f"जी हजुर {USER_NAME}! काम भयो।",
        f"भयो {USER_NAME}! के अरु सहयोग चाहियो?",
        f"All set {USER_NAME}! What's next?",
        f"Finished {USER_NAME}! Let me know if you need anything else."
    ]
    return random.choice(responses)

def get_error_response():
    """Response when command not understood"""
    responses = [
        f"Sorry {USER_NAME}, I didn't understand that. Can you please repeat? 🤔",
        f"Maile bujhina {USER_NAME}. फेरि भन्नुहोस्।",
        f"Command not recognized {USER_NAME}. Try saying 'help' for available commands.",
        f"Could you please rephrase that {USER_NAME}? I'm having trouble understanding.",
        f"माफ गर्नुहोस् {USER_NAME}! त्यो कमाण्ड मैले बुझिन।",
        f"I didn't catch that {USER_NAME}. Can you say it again?",
        f"Not sure what you mean {USER_NAME}. Please try again."
    ]
    return random.choice(responses)

def get_confirm_response():
    """Response when confirming an action"""
    responses = [
        f"Sure {USER_NAME}! 😊",
        f"Okay {USER_NAME}, on it! ⚡",
        f"Right away {USER_NAME}! 💫",
        f"जी हजुर {USER_NAME}!",
        f"Processing your request {USER_NAME}..."
    ]
    return random.choice(responses)