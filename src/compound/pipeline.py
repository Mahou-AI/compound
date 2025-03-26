from driver import get_driver

app = get_driver()


@app.get("/pipeline/tasks")
def tasks():
    return [
        "text-generation",
    ]
