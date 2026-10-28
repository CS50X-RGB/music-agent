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

def download_audio_batch(
    songs,
    output_directory: str = "temp",
) -> list[dict]:
    """
    Download audio for each song, convert it to MP3,
    upload it to S3, and return presigned playback URLs.

    Each song must contain:
        - title
        - url
        - video_id
    """

    if not songs:
        return []

    # Create an absolute output directory.
    output_directory = Path(output_directory).resolve()
    output_directory.mkdir(parents=True, exist_ok=True)

    # The session ID is the directory name.
    session_id = output_directory.name

    options = {
        "format": "bestaudio/best",
        "outtmpl": str(output_directory / "%(id)s.%(ext)s"),
        "noplaylist": True,
        "js_runtimes": {"node": {}},
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    # Download and convert the audio files.
    with yt_dlp.YoutubeDL(options) as ydl:
        for song in songs:
            try:
                ydl.download([song["url"]])
            except Exception as exc:
                print(
                    f"Download failed for {song.get('title', 'Unknown song')}: "
                    f"{exc}"
                )

    uploaded_songs = []

    # Upload successfully downloaded files to S3.
    for song in songs:
        video_id = song.get("video_id")

        if not video_id:
            print(f"Missing video_id for: {song.get('title', 'Unknown song')}")
            continue

        mp3_path = output_directory / f"{video_id}.mp3"

        if not mp3_path.is_file():
            print(f"MP3 not found: {mp3_path}")
            continue

        try:
            object_key = s3.upload_mp3(
                session_id=session_id,
                file_path=str(mp3_path),
            )

            playback_url = s3.get_playback_url(
                object_key=object_key,
                expires_in=900,
            )

            uploaded_songs.append(
                {
                    **song,
                    "mp3_path": str(mp3_path),
                    "s3_key": object_key,
                    "mp3_url": playback_url,
                }
            )

        except Exception as exc:
            print(
                f"S3 upload failed for {song.get('title', 'Unknown song')}: "
                f"{exc}"
            )

    return uploaded_songs