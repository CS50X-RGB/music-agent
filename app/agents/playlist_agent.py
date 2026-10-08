from app.llm.model import get_llm
from langchain_core.messages import SystemMessage
from app.agents.schema import MusicPlan

def playlist_agent(messages):
    llm = get_llm()

    system_message = SystemMessage(content="""

        You are the Playlist Orchestrator Agent.

        Your job is to understand the user's music request
        and decide what music operations are required.

        Available capabilities:

            - MusicBrainz:
            Find songs and music metadata.
            For MusicBrainz tasks, determine whether the user
            is asking about an artist or a specific song.
            Set search_type to either "artist" or "song".

            - Last.fm:
            Find artists similar to another artist.
            Last.fm tasks do not need a search_type.

        Task dependencies:

            - Each task has an index based on its position in the task list.
            - Use depends_on when a task needs the result of another task.
            - depends_on must contain the index of the task it depends on.
            - Use null when the task does not depend on another task.

        Example:

            If the user asks:
            "Give me Playboi Carti songs and songs from artists similar to him."

            Create:

            Task 0:
                agent = "Last.fm"
                query = "Playboi Carti"
                depends_on = null

            Task 1:
                agent = "MusicBrainz"
                query = "Find songs from the similar artists returned by Task 0"
                search_type = "artist"
                depends_on = 0

        This means Task 1 must wait for Task 0 and use its result.

        If the user only asks:
        "Give me Playboi Carti songs"

        Create:

            Task 0:
                agent = "MusicBrainz"
                query = "Playboi Carti"
                search_type = "artist"
                depends_on = null

        Do not generate the final playlist yet.
        First determine what information is needed.

    """)


    
    planner = llm.with_structured_output(MusicPlan)
    
    response = planner.invoke(
        [system_message] + messages
    )
    
    return response