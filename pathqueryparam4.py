from fastapi import FastAPI
import uvicorn

app=FastAPI()   # in function any value its call parameter like  def a(b) b means parameter
@app.get("/")  # if here any parameter we ue pu thats call path  parameter like @app.get("/men") men means path parameter this name we
# use after crome /that name pat
def index():
    return("hi prakash how are you")




## Path Parameter
# hare we change in path parameter like name on path   like  @app.get("/hello/{name}")  this is path aparameter

@app.get("/hello/{name}")      # this function like python user input(runtime variable) after run in crome change path like hello/prakash
def hello(name):       # we weite hello function and put name param
    return {"name":name}   # we writern hare name value
# http://127.0.0.1:8000/hello/prakash     # path parameter path




# Query Parameter       # we cgange in url here means what we need to change we change in url
@app.get("/hallo")
def hallo(name:str,subs:int): 
    return {"name":name,"subs":subs}
# http://127.0.0.1:8000/hallo?name=prakash&subs=1000  #query parameter                                            & thats call am perecent
