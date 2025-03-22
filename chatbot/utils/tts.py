import requests
import base64
from krutrim_cloud import KrutrimCloud
from dotenv import load_dotenv
import os

load_dotenv()

client = KrutrimCloud()


def speak(message):
    url = "https://cloud.olakrutrim.com/v1/audio/generations/krutrim-tts"

    payload = {
        "modelName": "tts",
        "input_text": message,
        "input_language": "en",
        "input_speaker": "female"
    }
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("KRUTRIM_CLOUD_API_KEY")}'
    }

    try:
        response = requests.post(url, json=payload, headers = headers)
        response.raise_for_status()  # Raise an error for HTTP failure codes

        x = response.json()
        base64_audio = x["output"]

        audio_data = base64.b64decode(base64_audio)
        
        with open("output_audio.wav", "wb") as f:
            f.write(audio_data)
        
        print("Audio file saved as output_audio.wav")
        return "Done"
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")