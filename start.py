from datetime import datetime
import os

from pathlib import Path
import fire
from openai import OpenAI

from dotenv import load_dotenv

AVAILABLE_MODELS = [
    "gpt-4",
    "gpt-4-0314",
    "gpt-4-32k",
    "gpt-4-32k-0314",
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-0301",
    "text-davinci-003",
    "code-davinci-002",
]

def validate_model(model):
    if model not in AVAILABLE_MODELS:
        raise ValueError(
            f"Invalid model '{model}', available models: {', '.join(AVAILABLE_MODELS)}"
        )

def get_timestamp():
    return datetime.now().strftime("%Y%b%d_%H-%M")

def get_own_prompt():
    while True:
        x = input("Enter your prompt: ")
        if (len(x) < 5):
            print("Prompt too short")
            continue
        else:
            return (x)

def read_and_clean_file(file_path, lower=False):
    with open(file_path, "r", encoding="utf-8") as f:
        context = clean(f.read(), lower=lower)
    return context

def save_output_to_file(
    out_dir,
    output,
    file_name,
):

    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    output_file = out_dir / file_name

    with output_file.open("w") as f:
        f.write(output)
def main():
    load_dotenv(),

    openai_api_key = os.environ.get("OPENAI_API_KEY", None)
    assert openai_api_key is not None, "OpenAI API key not found."
    model = "gpt-3.5-turbo"
    validate_model(model)

    client = OpenAI(
        # This is the default and can be omitted
        api_key=openai_api_key,

    )

    user_prompt = get_own_prompt()

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role":"user",
                "content":user_prompt
            }
        ],
        model=model,
        temperature=0.5,
        max_tokens=256,
        n=1,
        stop="null",
        presence_penalty=0,
        frequency_penalty=0.1
    )

    ts = get_timestamp()
    output_file_name = ts + "_response.txt"
    model_response = chat_completion.choices[0].message.content
    print(model_response)
    current_directory = os.getcwd()
    save_output_to_file(current_directory, model_response, output_file_name)

if __name__ == "__main__":
    fire.Fire(main)