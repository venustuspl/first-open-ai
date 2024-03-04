import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv(),

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get('OPENAI_API_KEY'),

)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Write weather in San francisco",
        }
    ],
    model="gpt-3.5-turbo",
)

model_response = chat_completion.choices[0].message.content
print(model_response)
