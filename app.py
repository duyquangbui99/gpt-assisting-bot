from chatbot import script, chat_with_gpt

if __name__ == "__main__":
    while True:
        user_input = input("User: ")
        query = script + user_input
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(query)
        print("Chatbot: ", response)
