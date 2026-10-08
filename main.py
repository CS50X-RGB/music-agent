from app.graph.workflow import app


def main():

    result = app.invoke({
        "messages": [
            ("user", "Give me Playboi Carti songs and artists similar to him")
        ],
        "plan": None,
        "results": []
    })

    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()