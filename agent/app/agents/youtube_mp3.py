import os
from pytube import YouTube
import moviepy.audio as mp

def download_video(title,url, output_directory):
    yt = YouTube(url)
    ys = yt.streams.filter(only_audio=False).first()
    video_output_path = os.path.join(output_directory, "`${title}.mp4`")
    ys.download(output_path=output_directory, filename="`${title}.mp4`")
    return video_output_path


def video_to_mp3(video_path, mp3_path):
    audio_clip = mp.AudioFileClip(video_path)
    audio_clip.write_audiofile(mp3_path)