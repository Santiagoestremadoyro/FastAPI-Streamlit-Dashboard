from fastapi import FastAPI
from routers import penguins


app = FastAPI()


@app.get("/")
def default():
    return{
        "API running correctly"
    }
