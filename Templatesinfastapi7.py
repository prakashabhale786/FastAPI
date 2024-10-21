# Step  1

# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# app=FastAPI()
# @app.get("/hallo")
# def hello():
#     ret='''
# <html>
# <body>
# <h2>Prakash Abhale</h2>
# </body>
# </html>
# '''
#     return HTMLResponse(content=ret)
#  http://127.0.0.1:8000/hallo     # path




# Step 2
#pip3 install jinja2
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,Request
app=FastAPI()
templates=Jinja2Templates(directory="templates")   # defult object
@app.get("/hello",response_class=HTMLResponse)  # it syd ki you have html file please take that file response  (index.html file in tanmplates)
def hello(request:Request):
    return templates.TemplatesResponse("index.html",{"request":request})

# http://127.0.0.1:8000/hallo 
# this file need index.html file