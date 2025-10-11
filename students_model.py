from pydantic import BaseModel
class Student(BaseModel):
    f_name:str
    l_name:str
    age:int
    school: str
    semester: int
    course: str
