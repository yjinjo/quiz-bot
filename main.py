from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/statc", StaticFiles(directory="static"), name="static")


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}

