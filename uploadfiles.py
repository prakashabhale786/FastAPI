from fastapi import FastAPI,File,UploadFile,Request
import uvicorn
import shutil
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
app=FastAPI()
templates=Jinja2Templates(directory="templates")
@app.get("/upload/",response_class=HTMLResponse)
def upload(request:Request):
    return templates.TemplateResponse("uploadfile.html",{"request":request})
@app.post("/uploder/")
def create_upload_file(file:UploadFile=File(...)):
    with open("destination.png","wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return {"filename":file.filename}