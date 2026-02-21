# Therapist Chatbot Project - PCAP Planning

# Goal:
# Build a rule-based "therapist" chatbot that interacts with the user, detects emotional keywords,
# and responds appropriately. User can quit at any time.

#    - Categories: SAD, ANGRY, ANXIOUS, HAPPY
#    - Each category has a list of keywords
emotion_keywords = {
    "sad": ["sad", "down", "unhappy"],
    "angry": ["angry", "mad", "frustrated"],
    "anxious": ["anxious", "nervous", "worried"],
    "happy": ["happy", "excited", "great"],
}
# Requirements / Features:
# 1. Collect user input in a loop until they type "quit"
function
while True:
    user_input = input(str("How are you feeling? "))
    # 5. Allow the user to type "quit" to exit
    if user_input == "quit":
        print("Goodbye!")
        break
    user_input = user_input.lower()

    # 2. Detect emotions in the input based on keywords
    detected_emotion = None
    for emotion, keywords in emotion_keywords.items():
        for keyword in keywords:
            if keyword in user_input:
                detected_emotion = emotion
                break
        if detected_emotion is not None:
            break


def response_to_emotion():
    # 3. Respond with an appropriate message based on detected emotion
    if detected_emotion == "sad":
        print("I'm sorry you're feeling sad today. Want to talk about it?")
    elif detected_emotion == "angry":
        print("I hear your frustration. Can you tell me more?")
    elif detected_emotion == "anxious":
        print("It sounds like you're worried. What's on your mind?")
    elif detected_emotion == "happy":
        print("That's great to hear! What made you feel this way?")
    # 4. If no keywords match, use a default response
    else:
        print("Oh? Tell me more...")


# 6. Optional: Track conversation history for the session

# Data Structures:
# - Dictionary: emotion_keywords = {emotion: [list of keywords]}
# - List: conversation_history (optional)

# Functions (optional, but PCAP-friendly):
# - detect_emotion(user_input) -> returns emotion category or None
# - respond_to_emotion(emotion) -> returns a string reply
## def detect_emotion():
##    """ placeholder """
## def respond_to_emotion(emotion):
##    """ placeholder """

# Program Flow:
# 1. Initialize emotion_keywords dictionary
# 2. Start a while loop for user interaction
# 3. Get input from the user
# 4. Check if user typed "quit" → break loop
# 5. Detect emotion from input
# 6. Generate appropriate response
# 7. Print response
# 8. Loop back to step 3

# Testing / Validation:
# - Test with sentences containing known keywords
# - Test with sentences containing no keywords
# - Test quit functionality
# - Optional: Test mixed-case inputs ("Sad" vs "sad")
