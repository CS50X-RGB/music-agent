from agent.app.llm.model import get_llm


def result_agent(messages, results, playlist):
    llm = get_llm()

    prompt = f"""
        You are the final Playlist Agent.

        User request:
        {messages[-1].content}

        Generated playlist:
        {playlist}

        Your task is to return the final playlist in the exact JSON structure below:

        {{
            "playlist_name": "Playlist Name",
            "session_id": "session-uuid",
            "songs": [
                {{
                    "id": "song-uuid",
                    "title": "Song Title",
                    "artist": "Artist Name",
                    "reason": "Why this song matches the user's prompt",
                    "duration" : "<duration of mp3 file using duration attribute of song>"
                    "audio_url": "<placeholder for the s3 bucket url link the mp3_url path from the object>"
                }}
            ]
        }}

    Rules:
    1. Return valid JSON only. Do not include Markdown code fences or explanations.
    2. Use "playlist_name" for the generated playlist's name.
    3. Use "session_id" for the playlist generation session ID, if available.
    4. Include every song from the generated playlist in the "songs" array.
    5. Each song must contain exactly these keys:
      "ID", "Title", "Artist", "Reason","Duration", "AudioUrl".
    6. Preserve actual song duration from the duration attribute.
    7. Duration must be returned as a its present in minute:second format like it coming from object as string.
    8. Never invent or estimate duration.
    9. Preserve the actual song IDs, titles, artists, reasons, and URLs from the available data.
      Never invent missing information.
    10. If a song has no audio URL, set "Audio Url" to "No Audio URL found".
    11. If a song ID is unavailable, use null.
    12. If the session ID is unavailable, use null.
    13. If the playlist name is unavailable, use "Untitled Playlist".
    14. Do not generate fake YouTube URLs or song details.
    15. Ensure the output is valid JSON with double-quoted keys and string values.
    16.Assign each song with ID like in number wise like 1 then the next object will be 2
  """

    response = llm.invoke(prompt)
    return response.content
