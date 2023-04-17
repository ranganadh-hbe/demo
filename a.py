#print("hello world")


# updated comments to track git...
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app=FastAPI()

@app.get('/')
def a():
    return {" Welcome ":"To Our Home Page"}


students=[{
    'name':'Ranga',
    'age':21

}]

class Student(BaseModel):
    name:Optional[str]
    age:Optional[int]


@app.post('/create_student')
def b(student:Student):
    if student:
        students.append(student)

        return student
    else:
        return {"Cannot add empty student..."}

@app.get('/get_student')
def c():
    return students