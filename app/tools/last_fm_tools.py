import pylast
import os
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()

LAST_FM_API_KEY = os.getenv("LASTFM_API_KEY")
LAST_FM_SHARED_KEY = os.getenv("LASTFM_API_SHARED_KEY")

@tool
def get_similar_artists(query : str):
    """
    Find artists similar to the given artist using Last.fm.

    Args:
        query: The name of the artist for which similar artists
            should be found.

    Returns:
        A list of PyLast artist objects similar to the given artist.
    """

    network = pylast.LastFMNetwork(
        api_key=LAST_FM_API_KEY,
        api_secret=LAST_FM_SHARED_KEY
    )
    
    artist = network.get_artist(query)
    similar_artists = artist.get_similar()
    return similar_artists