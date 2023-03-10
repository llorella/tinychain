import openai
import os

openai.api_key = (os.environ.get('OPENAI_API_KEY'))

def get_completion(model: str, messages: list[dict]) -> str:
    print(messages)
    completion = openai.ChatCompletion.create(
        model = model,
        messages= messages,
        max_tokens = 100,
        temperature = 0.9)
    return completion.choices[0].message.content


#next function logs token usage by messages sent by all three roles