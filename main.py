import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hello!", "Greetings!", "Hi!"],
    "how are you": ["I'm fine!", "Doing great!", "All good!"],
    "your name": ["I am a chatbot.", "You can call me ChatBot."],
    "help": ["I can chat with you. Try saying hello!"],
}

default_responses = [
    "I don't understand that.",
    "Can you rephrase?",
    "Interesting... tell me more!"
]

def chatbot():
    print("Chatbot: Hello! Type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        found = False

        for key in responses:
            if key in user_input:
                print("Chatbot:", random.choice(responses[key]))
                found = True
                break

        if not found:
            print("Chatbot:", random.choice(default_responses))


# Run chatbot
chatbot()
