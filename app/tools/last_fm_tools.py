import pylast
import os
from dotenv import load_dotenv
from langchain_core.tools import tool
import json

load_dotenv()

LAST_FM_API_KEY = os.getenv("LASTFM_API_KEY")
LAST_FM_SHARED_KEY = os.getenv("LASTFM_API_SHARED_KEY")

@tool
def get_similar_artists(query: str) -> str:
    """
    Find artists similar to the given artist using Last.fm.

    Args:
        query: Artist name to find similar artists for.

    Returns:
        A JSON string containing similar artists and their match scores.
    """

    network = pylast.LastFMNetwork(
        api_key=LAST_FM_API_KEY,
        api_secret=LAST_FM_SHARED_KEY
    )

    artist = network.get_artist(query)

    similar_artists = artist.get_similar()

    result = [
        {
            "artist": str(similar.item.name),
            "match": str(similar.match * 100)
        }
        for similar in similar_artists
    ]

    if not result:
        return "No similar artists found."

    return json.dumps(result)

