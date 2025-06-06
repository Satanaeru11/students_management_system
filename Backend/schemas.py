from pydantic import BaseModel
from typing import Optional

class JuniorHighSchoolBase(BaseModel):
    name: str
    principal: str
    contact_person: str
    address: str

class JuniorHighSchoolCreate(JuniorHighSchoolBase):
    pass

class JuniorHighSchool(JuniorHighSchoolBase):
    id: int
    model_config = {
        'from_attributes' : True
    }

class StudentBase(BaseModel):
    name: str
    grade: str
    course: str
    qualifications: str
    junior_high_id: int

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    junior_high: Optional[JuniorHighSchool]
    model_config = {
        'from_attributes' : True
    }