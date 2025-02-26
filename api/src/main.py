from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    """
    Root endpoint that returns the status of the application.

    Returns:
        dict[str, str]: A dictionary containing the status of the application.
    """

    return {"status": "OK"}
