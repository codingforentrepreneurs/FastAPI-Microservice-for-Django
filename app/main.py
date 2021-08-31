import pathlib
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = pathlib.Path(__file__).parent
app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))
# REST API

@app.get("/", response_class=HTMLResponse) # http GET -> JSON
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "abc": 123})


@app.post("/") # http POST
def home_detail_view():
    return {"hello": "world"}