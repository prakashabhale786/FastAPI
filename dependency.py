# dependency injection refers to the macanishm where in
# object recives other objects that it depends on.

from fastapi import FastAPI
app=FastAPI()
@app.get("/user/")
def usr(id:str,name:str,age:int):
    return {"id":id,"name":name,"age":age}
@app.get("/admin/")
def admin(id:str,name:str,age:int):
    return{"id":id,"name":name,"age":age}



