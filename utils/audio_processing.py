from moviepy.editor import VideoFileClip, AudioFileClip

def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = "static/audio.wav"
    video.audio.write_audiofile(audio_path)
    return audio_path

def replace_audio(video_path, new_audio_path):
    video = VideoFileClip(video_path)
    new_audio = AudioFileClip(new_audio_path)
    video = video.set_audio(new_audio)
    output_path = "output/output_video.mp4"
    video.write_videofile(output_path, audio_codec='aac')
    return output_path
