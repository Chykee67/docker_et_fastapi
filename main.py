from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    name="chike"
    return {"message": f"Hello {name}"}