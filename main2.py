from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the Student model
class Student(BaseModel):
    name: str
    roll_no: int
    address: str
    age: int

# In-memory list to store students
students: List[Student] = []

# Endpoint to add a new student
@app.post("/students/", response_model=Student)
def create_student(student: Student):
    students.append(student)
    return student

# Endpoint to get the list of students
@app.get("/students/", response_model=List[Student])
def get_students():
    return students

# Endpoint to get a specific student by roll number
@app.get("/students/{roll_no}", response_model=Student)
def get_student(roll_no: int):
    for student in students:
        if student.roll_no == roll_no:
            return student
    return {"error": "Student not found"}

# Endpoint to delete a student by roll number
@app.delete("/students/{roll_no}", response_model=Student)
def delete_student(roll_no: int):
    for student in students:
        if student.roll_no == roll_no:
            students.remove(student)
            return student
    return {"error": "Student not found"}

# Run the app with: uvicorn your_filename:app --reload
