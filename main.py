# The Post,GET,PUT and DELETE methods pereform respectively create read update delete opretions
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
data=[]
class Book(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
@app.post("/book")    # crete
def add_book(book:Book):
    data.append(book.dict())
    return data
@app.get("/list")     # read
def get_books():
    return data
@app.put("/book/{id}")      # update
def add_book(id:int,book:Book):
    data[id-1]=book
    return data
@app.delete("/book/{id}")     # delete
def delete_book(id:int):
    data.pop(id-1)         # we gave condition to delete id1 
    return data



    # http://127.0.0.1:8000/docs  # and changes what we need to create read update delete