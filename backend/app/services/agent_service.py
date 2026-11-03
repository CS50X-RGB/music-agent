from agent.app.main import main


class AgentService:

    
    def generate_playlist(self,prompt:str) -> str:
        result = main(prompt)
        
        return result['status'],result['msg']