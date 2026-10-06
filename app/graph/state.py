from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

class MusicState(TypedDict):
    messages : Annotated[list,add_messages]
    
###We don't want every node to overwrite the previous messages.
# add_messages tells LangGraph:
#"When a node returns new messages,
# append/merge them into the existing conversation state."
