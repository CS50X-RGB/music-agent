from app.llm.model import get_llm


def result_agent(messages, results, playlist):
    llm = get_llm()

    prompt = f"""
    You are the final Playlist Agent.

    User request:
    {messages[-1].content}

    Generated playlist:
    {playlist}

    Instructions:
    - Display the playlist name prominently as a Markdown heading.
    - List every song with its title, artist, reason, and YouTube link.
    - Do not invent songs, artists, reasons, or URLs.
    - If a song has a YouTube URL, include it as a Markdown link:
      [Watch on YouTube](URL)
    - If a song has no YouTube URL, display "No YouTube link found".
    - Use a Markdown table with columns:
      #, Title, Artist, Reason, YouTube Link
    """

    response = llm.invoke(prompt)

    return response