from database.connect_db import Base
from sqlalchemy import Column, Integer, String

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    def __repr__(self) -> str:
        return f"Student(id={self.id}, name={self.name})"


    def to_dict(self) -> dict:
        return {"id": self.id, "name": self.name}
