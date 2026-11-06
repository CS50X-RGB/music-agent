from agent.app.main import main
import json

class AgentService:

    
    def generate_playlist(self,prompt:str) -> str:
        result = main(prompt)
        
        return int(result['status']),json.loads(result['msg'])