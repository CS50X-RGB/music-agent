from agent.app.main import main
import json

class AgentService:

    
    def generate_playlist(self,prompt:str) -> str:
        result = main(prompt)

        status = result["status"]
        msg = result["msg"]

        if status != 200:
            return status, msg

        return status, json.loads(msg)