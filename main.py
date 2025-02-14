from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"Message": "Let's restart"}