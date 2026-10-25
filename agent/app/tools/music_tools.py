from langchain_core.tools import tool
import httpx
from app.exception.MusicSearchError import MusicSearchError

BASE_URL = "https://musicbrainz.org/ws/2/recording"


@tool
def search_music(query: str, search_type: str) -> list:
    """Search for music using MusicBrainz."""

    musicbrainz_query = query

    if search_type == "artist":
        musicbrainz_query = f'artist:"{query}"'
    elif search_type == "song":
        musicbrainz_query = f'recording:"{query}"'
    else:
        raise MusicSearchError(
            message="Invalid search type. Use 'artist' or 'song'.",
            error_type="invalid_search_type"
        )

    params = {
        "query": musicbrainz_query,
        "fmt": "json",
        "limit": 4
    }

    headers = {"User-Agent": "music-agent/0.1"}

    try:
        response = httpx.get(
            BASE_URL,
            params=params,
            headers=headers,
            timeout=15.0
        )
        response.raise_for_status()

    except httpx.HTTPStatusError as e:
        status_code = e.response.status_code

        if status_code == 503:
            message = "MusicBrainz is temporarily unavailable. Please try again later."
        elif status_code == 429:
            message = "Too many requests to MusicBrainz. Please wait before retrying."
        else:
            message = f"MusicBrainz returned an HTTP error: {status_code}."

        print(f"\n❌ Music Search Error: {message}")

        raise MusicSearchError(
            message=message,
            status_code=status_code,
            error_type="http_error"
        ) from e

    except httpx.RequestError as e:
        message = "Could not connect to MusicBrainz. Check your internet connection."
        print(f"\n❌ Music Search Error: {message}")

        raise MusicSearchError(
            message=message,
            error_type="request_error"
        ) from e

    data = response.json()
    songs = []

    for record in data.get("recordings", []):
        artist_credit = record.get("artist-credit", [])
        artist = (
            artist_credit[0].get("name", "Unknown")
            if artist_credit else "Unknown"
        )

        songs.append({
            "title": record.get("title", "Unknown"),
            "artist": artist
        })

    if not songs:
        print(f"\n⚠️ No songs found for: {query}")

    return songs