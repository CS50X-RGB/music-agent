from app.agents.schema import Playlist
from app.tools.yotube_tools import search_youtube

def youtube_agent(playlist: Playlist) -> Playlist:
    """Find one youtbe video for each song in the playlist."""
    
    songs = [
        {"title": song.title,"artist" : song.artist}
        for song in playlist.songs
    ]
    
    results = search_youtube.invoke({"songs" : songs})
    
    for song,result in zip(playlist.songs,results):
        video = result.get("video")
        
        if video:
            song.video_id = video["video_id"]
            song.url = video["url"]
            song.embed_url = video["embed_url"]
            
    return playlist