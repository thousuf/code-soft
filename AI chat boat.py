# simple_chatbot.py

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Rule-based responses
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm here to help you!"
    elif "what is your name" in user_input:
        return "I'm a simple chatbot created to assist you."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that. Could you please rephrase?"

def main():
    print("Chatbot: Hi there! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'bye']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()