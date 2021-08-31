from fastapi import FastAPI

app = FastAPI()


@app.get("/") # http GET
def home_view():
    return {"hello": "world"}


@app.post("/") # http POST
def home_detail_view():
    return {"hello": "world"}