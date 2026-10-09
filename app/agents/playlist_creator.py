from app.llm.model import get_llm
from app.agents.schema import Playlist
from langchain_core.messages import SystemMessage


def playlist_creator(messages, results):

    llm = get_llm()

    prompt = SystemMessage(
        content=f"""
        You are the Playlist Creator Agent.

        User Request:
        {messages[-1].content}

        Music research results:
        {results}

        Create a playlist using only songs found in the research results.

        Rules:
        - Do not invent songs or artists.
        - Remove duplicate songs.
        - Include similar artists when relevant.
        - Create a balanced playlist.
        - Give the playlist a suitable name.
        """
    )

    creator = llm.with_structured_output(Playlist)
    
    return creator.invoke([prompt])
