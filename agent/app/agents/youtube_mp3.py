import os
import yt_dlp

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

def download_audio_batch(songs, output_directory: str = "temp"):
    os.makedirs(output_directory, exist_ok=True)

    options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(
            output_directory, "%(title)s .%(ext)s"
        ),
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

    results = []
    for song in songs:
        results.append({
            **song,
            "mp3_path": os.path.join(
                output_directory,
                f"{song['title']}.mp3"
            ),
        })

    return results
