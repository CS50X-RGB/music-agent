from app.graph.workflow import app


def main():

    result = app.invoke({
        "messages": [
            ("user", "Give me a playlist for Travis Scott and Playboi Carti")
        ],
        "plan": None,
        "results": []
    })

    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()