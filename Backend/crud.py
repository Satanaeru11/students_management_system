from sqlalchemy.orm import Session
from models import Student, JuniorHighSchool
from schemas import StudentCreate, JuniorHighSchoolCreate

def create_jhs(db: Session, school: JuniorHighSchoolCreate):
    db_school = JuniorHighSchool(**school.dict())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

def get_all_jhs(db: Session):
    return db.query(JuniorHighSchool).all()

def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(Student).all()

def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

def update_student(db: Session, student_id: int, student_data: StudentCreate):
    student = get_student_by_id(db, student_id)
    if student is None:
        return None
    for key, value in student_data.dict().items():
        setattr(student, key, value)
        db.commit()
        db.refresh(student)
        return student
    
def delete_student(db: Session, student_id: int):
    student = get_student_by_id(db, student_id)
    if student is None:
        return None
    db.delete(student)
    db.commit()
    return student

def get_students_by_name(db: Session, name: str):
    return db.query(Student).filter(Student.name.contains(name)).all()

def get_students_by_school_if(db: Session, school_id: int):
    return db.query(Student).filter(Student.school_id == school_id).all()

def get_jhs_by_id(db: Session, school_id: int):
    return db.query(JuniorHighSchool).filter(JuniorHighSchool.id == school_id).first()

def update_jhs(db: Session, school_id: int, school_data: JuniorHighSchoolCreate):
    school = get_jhs_by_id(db, school_id)
    if school is None:
        return None
    for key, value in school_data.dict().items():
        setattr(school, key, value)
    db.commit()
    db.refresh(school)
    return school

def delete_jhs(db: Session, school_id: int):
    school = get_jhs_by_id(db, school_id)
    if school is None:
        return None
    db.delete(school)
    db.commit()
    return school

def get_jhs_by_name(db: Session, name: str):
    return db.query(JuniorHighSchool).filter(JuniorHighSchool.name.contains(name)).all()
