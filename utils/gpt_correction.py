import requests

# Azure Whisper API details
AZURE_WHISPER_ENDPOINT = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"
AZURE_KEY = "22ec84421ec24230a3638d1b51e3a7dc"

def transcribe_audio(audio_file_path):
    headers = {
        "api-key": AZURE_KEY,
        "Content-Type": "audio/mp4"  # Adjust based on the format of the audio you're sending (e.g., audio/mpeg, audio/wav)
    }

    with open(audio_file_path, "rb") as audio_file:
        response = requests.post(AZURE_WHISPER_ENDPOINT, headers=headers, data=audio_file)

    if response.status_code == 200:
        result = response.json()
        return result["text"]  # Returns the transcription
    else:
        raise Exception(f"Error with Whisper transcription: {response.text}")
