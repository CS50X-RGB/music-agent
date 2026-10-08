from app.llm.model import get_llm


def result_agent(messages, results):

    llm = get_llm()
    prompt = f"""
    You are the final Playlist Agent.

    The user asked:
    {messages[-1].content}

    The music agents returned these results:
    {results}
     
    Use these results to answer the user clearly.
    Give combine the songs in the table only dont need the similar artist table
    Do not invent songs or artists.
    """

    response = llm.invoke(prompt)

    return response