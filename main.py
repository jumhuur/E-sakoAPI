from bson import ObjectId
from fastapi import FastAPI, HTTPException
from students_model import Student
from database import collection
from Dahab import xisaab_Dahab
from Lacag import Lacag
from Fido import Fido
from Rikaas import Rikaas
from Geel import Geel
from Errors import Errors
#app
app = FastAPI(title="E-sako API", version="1.01")


@app.get("/")
def home():
    return {"code" : 200, "Fariin": "ku soo dhawaaw E-sako API"}


@app.get("/api/dahab/{nooc},{xadiga}")
def xisaab(nooc:int,xadiga:float):
    if nooc and xadiga:
        return xisaab_Dahab(nooc,xadiga)
    raise Errors(467)

@app.get("/api/lacag/{xadi}")
def lacag(xadi:int):
    if xadi:
        return Lacag(xadi)
    else:
        raise Errors(467)



@app.get("/api/fido/{xadi}")
def Fido_sako(xadi:int):
    if xadi:
        return Fido(xadi)
    else:
        return Errors(467)


@app.get("/api/rikaas/{xadi}")
def Rikaas_xisaab(xadi:int):
    if xadi:
        return Rikaas(xadi)
    else:
        return Errors(467)

@app.get("/api/geel/{xadi}")
def xisaab_geel(xadi:int):
    if xadi:
        return Geel(xadi)
    else:
        return Errors(467)


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
