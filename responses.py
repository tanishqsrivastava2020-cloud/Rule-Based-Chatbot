import random

# Predefined responses
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hello!", "Greetings!", "Hi!"],
    "courses": [
        "You have courses like CSE, CSA, Mathematics, Physics, etc.",
        "Your subjects include programming, mathematics, and core engineering courses."
    ],
    "deadline": [
        "Your project deadline is 31st March. Stay focused!",
        "Make sure to submit before 31st March to avoid penalties."
    ],
    "study": [
        "Study daily, revise concepts, and practice coding.",
        "Break your study into small sessions for better focus."
    ],
    "motivation": [
        "Stay consistent, success follows discipline 💪",
        "Small progress every day leads to big success!"
    ],
    "help": [
        "You can ask me about courses, deadlines, or study tips.",
        "Try asking: courses, deadline, or study."
    ]
}

# Default responses if nothing matches
default_responses = [
    "I didn't understand that.",
    "Can you rephrase your question?",
    "I'm still learning, try asking something else!"
]


def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return random.choice(default_responses)
