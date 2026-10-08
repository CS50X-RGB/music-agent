from app.graph.state import MusicState
# from app.llm.model import get_llm
# from app.tools.music_tools import search_music
# from app.tools.last_fm_tools import get_similar_artists
# from langgraph.prebuilt import ToolNode,tools_condition
from langgraph.graph import StateGraph,START,END
from app.agents.playlist_agent import playlist_agent
from app.agents.plan_executor import execute_plan
from app.agents.result_agent import result_agent

def result_node(state : MusicState):
    response = result_agent(
        state["messages"],
        state["results"]
    )
    
    return {
        "messages" : [response]
    }

def orchestrator_node(state : MusicState):
    plan = playlist_agent(state["messages"])
    
    return {
        "plan" : plan
    }

def executor_node(state : MusicState):
    results = execute_plan(state["plan"])
    
    return {
        "results" : results
    }
    

# def agent_node(state: MusicState):

#     llm = get_llm()

#     llm = llm.bind_tools([
#         search_music,
#         get_similar_artists
#     ])

#     response = llm.invoke(state["messages"])

#     return {
#         "messages": [response]
#     }
# ## this is a state so we need [] not response

# tool_node = ToolNode([
#     search_music,
#     get_similar_artists
# ])



    
# means "LLM, you are allowed to request this tool. in in case of llm bind tools"
# Whereas:
# tool_node = ToolNode([search_music])
# means "When the LLM requests this tool, execute it."

graph = StateGraph(MusicState)
graph.add_node("orchestrator", orchestrator_node)
graph.add_node("executor", executor_node)
graph.add_node("result", result_node)

graph.add_edge(START, "orchestrator")
graph.add_edge("orchestrator", "executor")
graph.add_edge("executor", "result")
graph.add_edge("result", END)

app = graph.compile()

