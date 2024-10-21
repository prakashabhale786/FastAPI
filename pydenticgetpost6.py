#from typing import List
#from pydantic import BaseModel

#class Student(BaseModel):
#    id: int
 #   name: str
#    subjects: List[str] = []

#data = {
#    "id": 1,
#    "name": "DataScience",
#    "subjects": ["Python", "NPV", "EDA","STATS", "ML","MYSQL","TABLEAU"],
#}

#s1 = Student(**data)
#print(s1)



# Get requests are only used to request data(not modify)
# post is use to send data to a server to create /update a resource.

# Both get and post method is use to transfer data from client to server i HTTP protocol
# Defference between Post and Get method is that get carries request parameter appanded in URL strings
# Post carries request parameter in massage body wich makes it more source way of transfering data



import uvicorn
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field
app=FastAPI()
class  Student(BaseModel):
    id:int
    name:str=Field(None,title="name of student",max_length=10)
    subjects:List[str]=[]
@app.post("/students")
def student_data(s1:Student):
    return s1

# http://127.0.0.1:8000/docs     # firast step   # edit on crom thi add 0 to 1 string to prakash subj to data Science
# http://127.0.0.1:8000/students # link   Final link