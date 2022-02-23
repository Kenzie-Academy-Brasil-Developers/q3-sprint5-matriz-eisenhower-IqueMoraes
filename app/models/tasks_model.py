from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.tasks_categories import tasks_categories


@dataclass
class TasksModel(db.Model):
    id: int
    name: str
    description: str
    duration: int


    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)

    eisenhower_id = Column(Integer, ForeignKey('eisenhowers.id'), nullable=False)

    categories = relationship("CategoriesModel", secondary=tasks_categories, back_populates="tasks")