from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

#from ai import get_ai_response

#print("welcome to the ai chatbot")
#print("type exit or quit to end the conversation")

#while True:
    #user_input = input("You: ")
    #if user_input.lower() in ["exit", "quit"]:
    #print("Goodbye!")
    #break
    
    #response = get_ai_response(user_input)
    #print(f"Assistant: {response}")
if __name__ == '__main__':
    app.run(debug=True)