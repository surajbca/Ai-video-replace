import streamlit as st
import os
from utils.audio_processing import extract_audio, replace_audio
from utils.transcription import transcribe_audio
from utils.gpt_correction import correct_transcription
from utils.tts_generation import text_to_speech

# Ensure the 'static/' directory exists
if not os.path.exists('static'):
    os.makedirs('static')

st.title("AI Audio Replacement in Video")

# File uploader for video files
video_file = st.file_uploader("Upload Video", type=["mp4"])

if video_file:
    # Save the uploaded video to the 'static/' directory
    video_path = "static/uploaded_video.mp4"
    with open(video_path, "wb") as f:
        f.write(video_file.read())
    
    st.write("Processing video...")

    try:
        # Step 1: Extract audio from video
        audio_path = extract_audio(video_path)
        st.write("Audio extracted successfully.")

        # Step 2: Transcribe audio
        transcription = transcribe_audio(audio_path)
        st.write(f"Original Transcription: {transcription}")

        # Step 3: Correct transcription using GPT-4o
        corrected_text = correct_transcription(transcription)
        st.write(f"Corrected Transcription: {corrected_text}")

        # Step 4: Convert corrected text to speech
        new_audio_path = text_to_speech(corrected_text)
        st.write("New audio generated successfully.")

        # Step 5: Replace audio in video
        output_video_path = replace_audio(video_path, new_audio_path)
        st.write("Audio replaced in video.")

        # Display the final video with replaced audio
        st.video(output_video_path)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
