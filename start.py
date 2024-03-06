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
            "role":"user",
            "content":"write a poem about the java developer work",
        }
    ],
    model="gpt-3.5-turbo",
    temperature=0.5,
    max_tokens=256,
    n=1,
    stop="null",
    presence_penalty=0,
    frequency_penalty=0.1
)

model_response = chat_completion.choices[0].message.content
print(model_response)
