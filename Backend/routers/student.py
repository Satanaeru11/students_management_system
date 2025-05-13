from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud, schemas

router = APIRouter(prefix='/students')

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

@router.get('/{student_id}', response_model=schemas.Student)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student_by_id(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail='Student not found')
    return student

@router.put('/{student_id}', response_model=schemas.Student)
def update_student(student_id: int, student: schemas.StudentCreate, db: Session = Depends(get_db)):
    update_student = crud.update_student(db, student_id, student)
    if update_student is None:
        raise HTTPException(status_code=404, detail='Student not found')
    return update_student

@router.delete('/{student_id}', response_model=schemas.Student)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    deleted_student = crud.delete_student(db, student_id)
    if deleted_student is None:
        raise HTTPException(status_code=404, detail='Student not found')
    return deleted_student

@router.get('/search/', response_model=list[schemas.Student])
def search_students_by_name(name: str, db: Session = Depends(get_db)):
    return crud.get_students_by_name(db, name)

@router.get('/by_school/{school_id}', response_model=list[schemas.Student])
def search_students_by_school(school_id: int, db: Session = Depends(get_db)):
    return crud.gets_students_by_schoool_id(db, school_id)