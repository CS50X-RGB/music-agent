import json

from agent.app.main import main


class AgentService:
    def generate_playlist(self, prompt: str) -> tuple:
        result = main(prompt)
        status = result["status"]
        msg = result["msg"]

        if status != 200:
            return status, msg

        return status, json.loads(msg)
