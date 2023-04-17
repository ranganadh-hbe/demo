#print("hello world")
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app=FastAPI()

@app.get('/')
def a():
    return {" Welcome ":"To Our Home Page"}


student={
    'name':'Ranga',
    'age':21

}

class Student(BaseModel):
    name:Optional[str]
    age:Optional[int]


@app.post('/create_student')
def b(student:Student):
    return student




