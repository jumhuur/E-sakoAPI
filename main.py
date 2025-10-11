from gc import collect
from bson import ObjectId
from fastapi import FastAPI, HTTPException
import Dahab
from students_model import Student
from database import collection
from Dahab import xisaab_Dahab
#app
app = FastAPI(title="E-sako API", version="1.01")

@app.get("/{dahab}/{nooc},{xadiga}")
def home(nooc:int,xadiga:float,dahab:str):
    if dahab:
        return xisaab_Dahab(nooc,xadiga)
    raise ValueError("nooca xadiga labadaaba waa loo bahan yahay")
    


@app.get("/students")
def get_students():
    Students = []
    for student in collection.find():
        student["_id"] = str(student["_id"])
        Students.append(student)
    return Students

@app.post("/students")
def add_students(new_student:Student):
    newstudent = collection.insert_one(new_student.model_dump())
    return f"id : { str(newstudent.inserted_id)}, waa la diwaan galiyay"


@app.put("/students/{Id}")
def update_student(Id:str,student_info:Student):
    student = collection.update_one({"_id": ObjectId(Id)}, {"$set":student_info.model_dump()})
    if student.modified_count == 1:
        return f"Waa La Cusboonaysiiyay"
    raise HTTPException(status_code=400, detail="qalad ayaa jira")


@app.delete("/student/{Id}")
def delete_student(Id:str):
    deleted = collection.delete_one({"_id": ObjectId(Id)})
    if deleted.deleted_count == 1:
        return "waa la masaxay"
    else:
        raise HTTPException(status_code=404, detail="ardaygan maan helin")
