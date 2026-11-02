from agent.app import main


class AgentService:

    
    def generate_playlist(self,prompt:str) -> str:
        result = main(prompt)
        
        return result["messages"][-1].content