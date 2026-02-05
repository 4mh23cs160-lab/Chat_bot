from ai import get_ai_response

print("welcome to the ai chatbot")
print("type exit or quit to end the conversation")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    
    response = get_ai_response(user_input)
    print(f"Assistant: {response}")