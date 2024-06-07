
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "what is your name": "I'm a chatbot created to assist you.",
    "bye": "Goodbye! Have a great day!"
}

def get_response(user_input):

    user_input = user_input.lower()


    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I didn't understand that."


def chatbot():
    print("Chatbot: Hi! I am a simple chatbot. You can talk to me by typing 'bye' to exit.")

    while True:

        user_input = input("You: ")


        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break


        response = get_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    chatbot()
