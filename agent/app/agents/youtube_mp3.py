import os
import yt_dlp
from app.aws.s3 import s3
from pathlib import Path

def download_audio(title: str, url: str, output_directory: str = "temp"):
    os.makedirs(output_directory, exist_ok=True)

    options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_directory, f"{title}.%(ext)s"),
        "noplaylist": True,
        "js_runtimes": {"node": {}},
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    mp3_path = os.path.join(output_directory, f"{title}.mp3")

    if not os.path.exists(mp3_path):
        raise FileNotFoundError(f"MP3 was not created: {mp3_path}")

    return mp3_path

def download_audio_batch(songs, output_directory="temp"):
    output_directory = Path(output_directory).resolve()
    output_directory.mkdir(parents=True, exist_ok=True)

    options = {
        "format": "bestaudio/best",
        "outtmpl": str(output_directory / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "js_runtimes": {"node": {}},
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    urls = [song["url"] for song in songs]

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download(urls)

    uploaded_songs = []

    # output_directory should be temp/<session_id>
    session_id = output_directory.name

    for song in songs:
        # Get the actual filename yt-dlp used
        file_path = output_directory / f"{song['title']}.mp3"

        if not file_path.is_file():
            raise FileNotFoundError(
                f"MP3 not found: {file_path}\n"
                f"Directory contents: {list(output_directory.iterdir())}"
            )

        object_key = s3.upload_mp3(
            session_id=session_id,
            file_path=str(file_path),
        )

        uploaded_songs.append({
            **song,
            "mp3_path": str(file_path),
            "s3_key": object_key,
            "mp3_url": s3.get_playback_url(object_key),
        })

    return uploaded_songs