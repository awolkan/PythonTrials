import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(""),
        UserMessage("Who invented the electricity first? Please explain in no more than 3 sentences"),
    ],
    temperature=1,
    top_p=1,
    model=model
)

print(response.choices[0].message.content)
'''
from openai import OpenAI

# Initialize the OpenAI client (it will automatically read OPENAI_API_KEY from environment)
client = OpenAI()

# Make a chat completion request
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4.1",  # Specify the desired model
)

print(chat_completion.choices[0].message.content)
'''
