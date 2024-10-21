from fastapi import FastAPI
import sqlite3

# app=FastAPI()
# @app.get("/")
# def add_name(studentname:str):
#     return{"result":studentname}      # http://127.0.0.1:8000/?studentname=Prakash


# insert record
app=FastAPI()
@app.get("/insert")
def add_name(studentname:str,age:int):
    conn=sqlite3.connect("website.db")
    conn.execute("insert into name (student,age) values(?, ?)",[studentname,age])
    conn.commit()
    conn.close()
    return{"result":studentname}         # http://127.0.0.1:8000/insert?studentname=Prakash