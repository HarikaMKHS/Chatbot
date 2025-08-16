# chatbot.py
def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "your name" in user_input:
        return "I'm your friendly chatbot 🤖"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure! I can answer simple questions. Try saying hello, ask my name, or say bye."
    else:
        return "Sorry, I didn’t understand that. Try something else!"
