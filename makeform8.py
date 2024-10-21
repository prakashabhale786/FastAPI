from fastapi import Form
from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app=FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/static",StaticFiles(dirctory="static"),name="static")
@app.get("/login",response_class=HTMLResponse)
def login(request:Request):
    return templates.TemplateResponse("login.html",{"request":request})
@app.post("/submit")
def submit(nm:str=Form(...), pwd:str = Form(...)):
    return {"username":nm}



# FastAPI as a form class to process the data recived as a request by submitting an html form.
# pip3 install python-multipart