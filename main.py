from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    name="chikeluba"
    return {"message": f"Hello {name}"}