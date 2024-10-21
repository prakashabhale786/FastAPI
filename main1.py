from fastapi import FastAPI


# every path name we can write the deferent and run and in crome / after we use thatname (path parameter name)
app=FastAPI()  # THis is the object on fastapi  # app means object name we can change app name what we want # fastapi this is the functio
@app.get("/")  # We create the path# this is the path creater line we create here path in bracket when we create the path we need @ before the app
async def index():  # we use index() to gave commond return all
    return("hi prakash")      # index function run this commond



#output is hi prakash