import os
import yt_dlp
from yt_dlp.utils import sanitize_filename
from agent.app.aws.s3 import s3
from pathlib import Path
import re, unicodedata


def download_audio(title: str, url: str, output_directory: str = "temp"):
    os.makedirs(output_directory, exist_ok=True)

    options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(output_directory, f"{title}.%(ext)s"),
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

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

    mp3_path = os.path.join(output_directory, f"{title}.mp3")

    if not os.path.exists(mp3_path):
        raise FileNotFoundError(f"MP3 was not created: {mp3_path}")

    return mp3_path


def normalize_title(title: str) -> str:
    title = unicodedata.normalize("NFKD", title)
    title = title.lower().strip()
    title = re.sub(r"[^\w\s-]", "", title)
    title = re.sub(r"\s+", "-", title)
    return title


def download_audio_batch(songs, output_directory="temp"):

    output_directory = Path(output_directory).resolve()
    output_directory.mkdir(parents=True, exist_ok=True)

    session_id = output_directory.name
    uploaded_songs = []

    for song in songs:
        url = song["url"]

        # Step 1: Extract YouTube metadata
        metadata_options = {
            "quiet": True,
            "noplaylist": True,
            "js_runtimes": {"node": {}},
        }

        with yt_dlp.YoutubeDL(metadata_options) as ydl:
            info = ydl.extract_info(url, download=False)

        actual_title = info["title"]
        video_id = info["id"]

        safe_title = sanitize_filename(actual_title)

        # Avoid filename collisions
        filename = f"{safe_title}_{video_id}"

        # Step 2: Download audio
        options = {
            "format": "bestaudio/best",
            "outtmpl": str(output_directory / f"{filename}.%(ext)s"),
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

        with yt_dlp.YoutubeDL(options) as downloader:
            downloader.download([url])

        # Step 3: Verify MP3
        mp3_path = output_directory / f"{filename}.mp3"

        if not mp3_path.is_file():
            raise FileNotFoundError(
                f"MP3 not found: {mp3_path}\n"
                f"Downloaded files: {list(output_directory.iterdir())}"
            )

        # Step 4: Upload to S3
        object_key = s3.upload_mp3(
            session_id=session_id,
            file_path=str(mp3_path),
        )

        # Step 5: Save result
        uploaded_songs.append(
            {
                **song,
                "title": actual_title,
                "mp3_path": str(mp3_path),
                "s3_key": object_key,
                "mp3_url": s3.get_playback_url(object_key),
            }
        )

    return uploaded_songs
