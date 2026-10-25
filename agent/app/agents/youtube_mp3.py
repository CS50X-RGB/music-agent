import os
from moviepy import AudioFileClip
import yt_dlp

# def download_video(title: str, url: str, output_directory: str):
#     try:
#         print(f"\n🎵 Starting download: {title}")
#         print(f"🔗 URL: {url}")

#         os.makedirs(output_directory, exist_ok=True)

#         filename = f"{title}.%(ext)s"
#         video_output_path = os.path.join(output_directory, filename)

#         options = {
#             "format": "bestaudio/best",
#             "outtmpl": os.path.join(output_directory, f"{title}.%(ext)s"),
#             "noplaylist": True,
#             "js_runtimes": {"node": {}},
#             "postprocessors": [{
#                 "key": "FFmpegExtractAudio",
#                 "preferredcodec": "mp3",
#                 "preferredquality": "192",
#             }],
#         }
#         with yt_dlp.YoutubeDL({"listformats": True}) as ydl:
#             ydl.extract_info(url, download=False)

#         with yt_dlp.YoutubeDL(options) as ydl:
#             info = ydl.extract_info(url, download=False)
#             print(f"📀 Video found: {info.get('title', title)}")

#             print("⬇️ Downloading video...")
#             ydl.download([url])

#             # Resolve the actual output filename
#             actual_path = ydl.prepare_filename(info)

#         if not os.path.exists(actual_path):
#             raise FileNotFoundError(
#                 "Download finished, but the video file was not found."
#             )

#         print(f"✅ Download successful: {actual_path}")
#         return actual_path

#     except Exception as e:
#         print(f"\n❌ Download failed for: {title}")
#         print(f"   Error type: {type(e).__name__}")
#         print(f"   Reason: {e}")
#         raise

# def video_to_mp3(video_path: str, mp3_path: str):
#     try:
#         print(f"\n🎧 Converting to MP3: {video_path}")

#         with AudioFileClip(video_path) as audio_clip:
#             audio_clip.write_audiofile(mp3_path)

#         if not os.path.exists(mp3_path) or os.path.getsize(mp3_path) == 0:
#             raise RuntimeError("MP3 conversion failed or produced an empty file.")

#         print(f"✅ MP3 created: {mp3_path}")

#         os.remove(video_path)
#         print("🗑️ Temporary MP4 deleted.")

#         return mp3_path

#     except Exception as e:
#         print("\n❌ Audio conversion failed")
#         print(f"   Error type: {type(e).__name__}")
#         print(f"   Reason: {e}")
# #         raise


# def yt_to_mp3_local(title: str, url: str, output_directory: str = "temp"):
#     try:
#         video_path = download_video(title, url, output_directory)

#         mp3_path = os.path.splitext(video_path)[0] + ".mp3"

#         return video_to_mp3(video_path, mp3_path)

#     except Exception as e:
#         print(f"\n❌ Audio retrieval pipeline failed for: {title}")
#         print(f"   Reason: {e}")
#         raise
    
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
