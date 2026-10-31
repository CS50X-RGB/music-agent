from agent.app.main.main import main

class AgentService:

    
    def generate_playlist(self,prompt:str) -> str:
        result = main(prompt)
        
        return result["messages"][-1].content