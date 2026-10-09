from app.agents.playlist_agent import playlist_agent
from app.agents.plan_executor import execute_plan
from app.agents.result_agent import result_agent
from app.agents.playlist_creator import playlist_creator
from app.graph.state import MusicState
from app.agents.yotube_agent import youtube_agent

def result_node(state : MusicState):
    response = result_agent(
        state["messages"],
        state["results"],
        state["playlist"]
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
    
def playlist_creator_node(state : MusicState):
    playlist = playlist_creator(state["messages"],state["results"])

    return {
        "playlist": playlist
    }
    
def youtube_agent_node(state : MusicState):
    playlist = state["playlist"]
    
    updated_playlist = youtube_agent(playlist)
    
    return  {
        "playlist" : updated_playlist
    }