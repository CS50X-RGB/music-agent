from app.graph.workflow import app

def main():
    result = app.invoke({
        "messages": [
            ("user", "Suggest me some Playboi Carti songs where Travis Scott is featured artist")
        ]
    })

    print(result["messages"][-1].content)

    
if __name__ == "__main__":
    main()
