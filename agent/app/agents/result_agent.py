from app.llm.model import get_llm


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
                    "ID": "song-uuid",
                    "Title": "Song Title",
                    "Artist": "Artist Name",
                    "Reason": "Why this song matches the user's prompt",
                    "Audio Url": "https://www.youtube.com/watch?v=example"
                }}
            ]
        }}

    Rules:
    1. Return valid JSON only. Do not include Markdown code fences or explanations.
    2. Use "playlist_name" for the generated playlist's name.
    3. Use "session_id" for the playlist generation session ID, if available.
    4. Include every song from the generated playlist in the "songs" array.
    5. Each song must contain exactly these keys:
      "ID", "Title", "Artist", "Reason", "Audio Url".
    6. Preserve the actual song IDs, titles, artists, reasons, and URLs from the available data.
      Never invent missing information.
    7. If a song has no audio URL, set "Audio Url" to "No Audio URL found".
    8. If a song ID is unavailable, use null.
    9. If the session ID is unavailable, use null.
    10. If the playlist name is unavailable, use "Untitled Playlist".
    11. Do not generate fake YouTube URLs or song details.
    12. Ensure the output is valid JSON with double-quoted keys and string values.
  """

    response = llm.invoke(prompt)
    return response.content
