from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    name="baby"
    return {"message": f"Hello {name}"}