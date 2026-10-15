
# Basic Chatbot using a Dictionary

responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! How are you?",
    "how are you": "I'm fine, thanks! How about you?",
    "what is your name": "I'm a Python chatbot.",
    "who created you": "I was created using Python.",
    "thank you": "You're welcome!",
    "good morning": "Good morning! Have a great day!",
    "good night": "Good night! Sweet dreams!",
    "bye": "Goodbye! Have a great day!",
    "exit": "Goodbye! Have a great day!"
}

print("Chatbot: Hello! Welcome to my chatbot.")
print("Chatbot: Type 'bye' or 'exit' to end the conversation.")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["bye", "exit"]:
        print("Chatbot:", responses[user_input])
        break

    elif user_input in responses:
        print("Chatbot:", responses[user_input])

    else:
        print("Chatbot: Sorry, I don't understand that yet.")
