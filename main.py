from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    name="baby"
    return {"message": f"Hey baby\nBest of luck in your exams\nI love you always"}