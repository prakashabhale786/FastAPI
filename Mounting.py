# we create here 2 object
from fastapi import FastAPI
app=FastAPI()
@app.get("/app")
def mainindex():
    return {"message":"Hello Prakash What are you doing"}  #http://127.0.0.1:8000/app
subapp=FastAPI()
@subapp.get("/sub")
def subindex():
    return {"message":"hey hi i am a Data Analyst"}
app.mount("/subapp",subapp)

# http://127.0.0.1:8000/sub

#http://127.0.0.1:8000/docs