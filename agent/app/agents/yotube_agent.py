from app.agents.schema import Playlist
from app.tools.yotube_tools import search_youtube
from app.agents.youtube_mp3 import download_audio_batch
import os,uuid,shutil

def youtube_agent(playlist: Playlist) -> Playlist:
    """Find one youtbe video for each song in the playlist."""
    
    songs = [
        {"title": song.title,"artist" : song.artist}
        for song in playlist.songs
    ]
    
    results = search_youtube.invoke({"songs" : songs})
    session_id = str(uuid.uuid4())
    session_dir = os.path.join("temp", session_id)
    os.makedirs(session_dir, exist_ok=True)
    batch = []
    for song,result in zip(playlist.songs,results):
        video = result.get("video")

        if video:
            song.video_id = video["video_id"]
            song.url = video["url"]
            song.embed_url = video["embed_url"]
            batch.append({
                    "title" : song.title,
                    "url" : video["url"],
                    "video_id" : video["video_id"]
            })
    
    download = download_audio_batch(batch,session_dir)
    shutil.rmtree(session_dir, ignore_errors=True)
    playlist.session_id = session_id
    for song, audio in zip(
        [s for s in playlist.songs if s.video_id],
        download
    ):
        song.mp3_url = audio["mp3_url"] # AWS LINK
        
    return playlist

