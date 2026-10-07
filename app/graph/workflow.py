from app.graph.state import MusicState
from app.llm.model import get_llm
from app.tools.music_tools import search_music
from app.tools.last_fm_tools import get_similar_artists
from langgraph.prebuilt import ToolNode,tools_condition
from langgraph.graph import StateGraph,START


def agent_node(state: MusicState):

    llm = get_llm()

    llm = llm.bind_tools([
        search_music,
        get_similar_artists
    ])

    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }
## this is a state so we need [] not response

tool_node = ToolNode([
    search_music,
    get_similar_artists
])

    
# means "LLM, you are allowed to request this tool. in in case of llm bind tools"
# Whereas:
# tool_node = ToolNode([search_music])
# means "When the LLM requests this tool, execute it."

graph = StateGraph(MusicState)
graph.add_node("agent", agent_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "agent")

graph.add_conditional_edges(
    "agent",
    tools_condition
)

graph.add_edge("tools", "agent")

app = graph.compile()

