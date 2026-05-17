# from rapidfuzz import fuzz

# INTENTS = {
#     "open": ["open", "start", "launch", "khola", "khol"],
#     "search": ["search", "find", "lookup"],
#     "close": ["close", "band", "banda"],
#     "play": ["play", "sunau", "baja"],
#     "pause": ["pause", "rok"],
#     "back": ["back", "pachadi"],
#     "scroll": ["scroll", "move"]
# }

# TOOLS = [
#     "youtube", "google", "facebook", "instagram", "gmail", "chatgpt"
# ]

# def detect_intent(command):
#     best = ("unknown", 0)

#     for intent, words in INTENTS.items():
#         for w in words:
#             score = fuzz.partial_ratio(w, command)
#             if score > best[1]:
#                 best = (intent, score)

#     return best[0]


# def extract_entity(command):
#     for tool in TOOLS:
#         if tool in command:
#             return tool
#     return command.strip()