from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(directory="static"),name="static")
@app.get("/hello/{name}",response_class=HTMLResponse)
def hello(request:Request,name:str):
     return templates.TemplatesResponse("index.html",{"request":request,"name":name})