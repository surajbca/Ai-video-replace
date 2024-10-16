from moviepy.editor import VideoFileClip

def extract_audio(video_path):
    try:
        video = VideoFileClip(video_path)
        audio_path = "static/extracted_audio.wav"  # Save as .wav for better transcription results
        video.audio.write_audiofile(audio_path)
        video.close()  # Close the video file to release resources
        return audio_path
    except Exception as e:
        raise RuntimeError(f"Error extracting audio: {str(e)}")
