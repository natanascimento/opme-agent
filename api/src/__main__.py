import uvicorn


def start():
    uvicorn.run("__init__:api", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()