import os
import httpx

from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()


@tool
def search_youtube(songs: list[dict]) -> list[dict]:
    """Search YouTube for music videos matching song titles and artists.

    Args:
        songs: List of dictionaries containing title and artist.

    Returns:
        A list of songs with their matching YouTube video details.
    """
    api_key = os.getenv("YOUTUBE_API_KEY")

    if not api_key:
        return []

    url = "https://www.googleapis.com/youtube/v3/search"
    results = []

    for song in songs:
        title = song["title"]
        artist = song["artist"]

        params = {
            "part": "snippet",
            "q": f'"{title}" "{artist}"',
            "type": "video",
            "videoCategoryId": "10",
            "videoEmbeddable": "true",
            "maxResults": 3,
            "key": api_key,
        }

        try:
            response = httpx.get(url, params=params, timeout=15)
            response.raise_for_status()
            data = response.json()

            videos = []

            for item in data.get("items", []):
                video_id = item["id"]["videoId"]
                snippet = item["snippet"]

                videos.append({
                    "title": snippet["title"],
                    "channel": snippet["channelTitle"],
                    "video_id": video_id,
                    "url": f"https://www.youtube.com/watch?v={video_id}",
                    "embed_url": f"https://www.youtube.com/embed/{video_id}",
                })
            best_video = videos[0] if videos else None
            results.append({
                "song": title,
                "artist": artist,
                "video": best_video,
            })                 

        except httpx.HTTPError:
            results.append({
                "song": title,
                "artist": artist,
                "videos": [],
                "error": "YouTube search request failed",
            })

    return results

