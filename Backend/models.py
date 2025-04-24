from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class JuniorHighSchool(Base):
    __tablename__ = "junior_high_schools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    principal = Column(String)
    contact_person = Column(String)
    address = Column(String)

    students = relationship("Student", back_populates="junior_high")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    grade = Column(String)
    course = Column(String)
    qualifications = Column(String)

    junior_high_id = Column(Integer, ForeignKey("junior_high_schools.id"))
    junior_high = relationship("JuniorHighSchool", back_populates="students")
