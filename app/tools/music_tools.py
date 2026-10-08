from langchain_core.tools import tool
import httpx

BASE_URL = "https://musicbrainz.org/ws/2/recording"

@tool
def search_music(query : str,search_type : str) -> str:
    """
        Search for music using MusicBrainz
        
        Args:
            query: Artist name, song title, or music search term.
            search_type: Type of search. Must be 'artist' or 'song'.
        Returns:
            A list of songs containing title and artist information.
    """
    musicbrainz_query = query
    
    if search_type == "artist":
        musicbrainz_query = f'artist:"{query}"'
    elif search_type == "song":
        musicbrainz_query = f'recording:"{query}"'
    
    params = {
        "query" : musicbrainz_query,
        "fmt" : "json",
        "limit" : 3
    }
    
    headers = {
        "User-Agent" : "music-agent/0.1"
    }
    
    response = httpx.get(
        BASE_URL,
        params=params,
        headers=headers
    )
    
    response.raise_for_status()
    
    data = response.json()
  
    songs = []
    
    for record in data["recordings"]:
        artist = record['artist-credit'][0]['name']
        songs.append({
            "title": record["title"],
            "artist": artist
        })
    
    return songs