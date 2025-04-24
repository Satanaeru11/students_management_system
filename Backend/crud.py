from sqlalchemy.orm import Session
from models import Student, JuniorHighSchool
from schemas import StudentCreate, JuniorHighSchoolCreate

# 中学校
def create_jhs(db: Session, school: JuniorHighSchoolCreate):
    db_school = JuniorHighSchool(**school.dict())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

def get_all_jhs(db: Session):
    return db.query(JuniorHighSchool).all()

# 生徒
def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(Student).all()
