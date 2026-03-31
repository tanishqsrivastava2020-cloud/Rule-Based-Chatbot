from responses import get_response

def chatbot():
    print("Chatbot: Hello! What is your name?")
    name = input("You: ")

    print(f"Chatbot: Nice to meet you, {name}! Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print(f"Chatbot: Goodbye {name}! 👋")
            break

        response = get_response(user_input)
        print("Chatbot:", response)


chatbot()
