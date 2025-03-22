# Please add "stream : true" for faster responses
# pip install krutrim-cloud
from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv

load_dotenv()

client = KrutrimCloud()


def chat(message):
    model_name = "DeepSeek-R1-Llama-8B"
    messages = [
        {"role": "system", "content": "You are an AI Companion chatbot named Shanaya, you have to mimic being a human and establish a relationship with the user. Be nice to the person, get to know them. Respond like you are responding to texts without any expressive meta texts"},
        {"role": "user", "content": message}
    ]

    try:
        response = client.chat.completions.create(model=model_name, messages=messages)

        # Access generated output
        txt_output_data = response.choices[0].message.content  # type:ignore
        print(f"Output: \n{txt_output_data}")

        # OR
        # Save generated output
        # response.save(output_dirpath="./output")
        return txt_output_data
    except Exception as exc:
        print(f"Exception: {exc}")