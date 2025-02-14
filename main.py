from fastapi import FastAPI

app = FastAPI()

#entry point
@app.get('/')
def index():
    return {"Message": "Let's restart"}

@app.get('/name')
def name_page():
    return {"name": "chikeluba"}