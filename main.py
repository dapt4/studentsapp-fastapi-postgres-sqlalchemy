from fastapi import FastAPI
from models import models
from models.models import Student
from database.connect_db import engine, SessionLocal
from sqlalchemy import select, insert, delete, update
from utils.typing import StudentType

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def list():
    with SessionLocal() as db:
        students = db.query(Student).all()
        return students

@app.get("/student/{id}")
def get_one(id: int):
    with SessionLocal() as db:
        try:
            stmt = select(Student).where(Student.id == id)
            student = db.execute(stmt).one()
            response = student[0].to_dict()
            return response
        except Exception as err:
            print(err)
            return {"error:" "404 not found"}

@app.post("/student")
def new_student(student: StudentType):
    with SessionLocal() as db:
        try:
            student1 = Student(name=student.name)
            db.add(student1)
            db.commit()
            return student1.to_dict()
        except Exception as err:
            print(err)
            return {"error:" "501 internal server error"}

@app.delete('/student/{id}')
def delete_student(id: int):
    with SessionLocal() as db:
        try:
            stmt = delete(Student).where(Student.id == id)
            db.execute(stmt)
            db.commit()
            return {"status": "done"}
        except Exception as err:
            print(err)
            return {"error:" "501 internal server error"}

@app.put('/student/{id}')
def update_student(id: int, student: StudentType):
    with SessionLocal() as db:
        try:
            stmt = (update(Student).where(Student.id == id)
            .values(name=student.name))
            db.execute(stmt)
            db.commit()
            return student
        except Exception as err:
            print(err)
            return {"error:" "501 internal server error"}
