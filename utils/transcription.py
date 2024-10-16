from google.cloud import speech

def transcribe_audio(audio_path):
    client = speech.SpeechClient()
    with open(audio_path, "rb") as audio_file:
        audio_data = audio_file.read()

    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(language_code="en-US")

    response = client.recognize(config=config, audio=audio)
    transcription = ' '.join([result.alternatives[0].transcript for result in response.results])
    return transcription
