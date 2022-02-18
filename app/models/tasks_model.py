from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String, Text



@dataclass
class TasksModel(db.Model):
    id = int
    name = str
    description = str
    duration = int
    importance = int
    urgency = int
    eisenhower_id = int

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhower_id = Column(Integer, ForeignKey('eisenhowers.id'), nullable=False)


    #para estudo
    # categories = relationship("CategoriesModel", secondary=tasks_categories, backref="categories")