# Basic Chatbot

def chatbot():
    print("your CHATBOT is live")
    print("Type hello, how are you, or bye")
    
    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("Bot: Hi!")

        elif message == "how are you":
            print("Bot: I'm fine, thanks!")

        elif message == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


# Start the chatbot
chatbot()