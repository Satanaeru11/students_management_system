from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.get("/", response_model=list[schemas.Student])
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)

@router.post("/schools/", response_model=schemas.JuniorHighSchool)
def create_school(school: schemas.JuniorHighSchoolCreate, db: Session = Depends(get_db)):
    return crud.create_jhs(db, school)

@router.get("/schools/", response_model=list[schemas.JuniorHighSchool])
def read_schools(db: Session = Depends(get_db)):
    return crud.get_all_jhs(db)
