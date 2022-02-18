from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref

@dataclass
class EisenhowersModel(db.Model):
    id = int
    type = str

    __tablename__ = "eisenhowers"

    id = Column(Integer, primary_key=True)
    type = Column(String(100))

    tasks = relationship("TasksModel", backref=backref("eisenhowers", uselist=False))