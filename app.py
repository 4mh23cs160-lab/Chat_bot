import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage, AssistantMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "gpt-4o-mini"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


messages = [
    SystemMessage(content="You are a helpful assistant."),
]

print("Chatbot started! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages.append(UserMessage(content=user_input))

    response = client.complete(
        messages=messages,
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model
    )

    bot_response = response.choices[0].message.content
    print(f"Assistant: {bot_response}")
    
    messages.append(AssistantMessage(content=bot_response))

