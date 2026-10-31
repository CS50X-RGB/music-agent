from app.graph.workflow import app
from app.gaurdrails.promptParser import MusicGuardrail

def main(user_prompt=""):
    guardrail = MusicGuardrail()
    
    if not guardrail.validate_prompt(user_prompt=user_prompt):
        return "Prompt is not good"
    
    result = app.invoke({
        "messages": [
            ("user", user_prompt)
        ],
        "plan": None,
        "results": []
    })

    return (result["messages"][-1].content)


if __name__ == "__main__":
    main()