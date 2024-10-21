# PATH VALIDATION            # python user input    # 1 variable use name
from fastapi import FastAPI,Path
app=FastAPI()
@app.get("/hllo/{name}")
def hllo(name:str=Path(...,min_length=3,max_length=10)):   # we gave the lenght condition of strings min3 max10 mean les then 10alphabates
     # str=path means we want to validation in name variable there we use path function
    #    (...,min_length=3,max_length=10)):         this is the validation
    return {"name":name}

# http://127.0.0.1:8000/hllo/prakash    # path validation path




# 2 variables use name and age
from fastapi import FastAPI,Path
app=FastAPI()
@app.get("/hello/{name}/{age}")
def hello(*, name:str=Path(...,min_length=3,max_length=10),age:int=Path(..., ge=1,le=100)):  # ge means grether then=to, le means lessthen =to
          # here we gave the 2 variables name and age
    return {"name":name,"age":age}

# http://127.0.0.1:8000/hello/prakash/27   # path


#ge(grether then = to),gt(greter then),le(less then=to),lt(less then)  4 variables we have  we use in validation


# when we use   Strings (name:str=Path(...,min_length=3,max_length=10))     ,    integer(age:int=Path(..., ge=1,le=100)):) like that


#QUERY VALIDATION
from fastapi import FastAPI,Path,Query
app=FastAPI()
@app.get("/hallo/{name}/{age}")
def hallo(*,name:str=Path(...,min_length=3,max_length=10),\
          age:int=Path(...,ge=1,le=100),\
            percent:int=Query(...,ge=0,le=100)):  # we takes percent function we wrote query means we want to change in query
           # query validation means we change here to use percent
    return {"name":name,"age":age}

# http://127.0.0.1:8000/hallo/prakash/14?percent=89       # path



