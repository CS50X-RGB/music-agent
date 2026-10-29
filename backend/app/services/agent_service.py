from agent.app.graph.workflow import app as graph

class AgentService:
    def __init__(self):
        self.graph = graph
    
    def generate_playlist(self,prompt:str) -> str:
        result = self.graph.invoke({
            "messages" : [
                {
                    "role" : "user",
                    "content" : prompt
                }
            ]
        })
        
        return result["messages"][-1].content