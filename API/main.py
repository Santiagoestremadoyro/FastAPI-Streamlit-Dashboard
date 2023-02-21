from fastapi import FastAPI
from router import pinguins, principal


app = FastAPI()

app.include_router(pinguins.router)
app.include_router(principal.router)

@app.get("/")
def default():
    return{
        "API running correctly"
    }
