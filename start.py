import os

from pathlib import Path
import fire
from openai import OpenAI

from dotenv import load_dotenv
def save_output_to_file(
    out_dir,
    output,
    file_name,
):
    """
    Saves the generated output to a file.
    :param out_dir: The output directory.
    :param output: The text to be saved.
    :param file_name: The name of the output file.
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    output_file = out_dir / file_name

    with output_file.open("w") as f:
        f.write(output)
def main():
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
    current_directory = os.getcwd()
    save_output_to_file(current_directory, model_response, 'response.txt')

if __name__ == "__main__":
    fire.Fire(main)