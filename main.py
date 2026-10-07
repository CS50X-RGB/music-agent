from app.graph.workflow import app

def main():
    result = app.invoke({
        "messages": [
            ("user", "Suggest me similar artist to Playboi Carti")
        ]
    })

    print(result["messages"][-1].content)

    
if __name__ == "__main__":
    main()
