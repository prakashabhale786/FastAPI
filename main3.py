from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
data = []

class Students(BaseModel):
    studentname: str
    studentrollno: int
    studentage: int
    studentaddress: str
    id:int

@app.post("/students")  # Create
def add_student(students: Students):
    data.append(students.dict())
    return students  # Return the created student

@app.get("/list")  # Read
def get_students():
    return data

@app.put("/students/{id}")  # Update
def update_student(id: int, students: Students):
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="Student not found")
    data[id - 1] = students.dict()  # Update the specific student
    return students

@app.delete("/students/{id}")  # Delete
def delete_student(id: int):
    if id < 1 or id > len(data):
        raise HTTPException(status_code=404, detail="Student not found")
    data.pop(id - 1)  # Remove the specific student
    return {"message": "Student deleted successfully"}

