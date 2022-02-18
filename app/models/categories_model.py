from dataclasses import dataclass
from app.configs.database import db
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.models.tasks_categories import tasks_categories


@dataclass
class CategoriesModel(db.Model):
    id: int
    name: str
    description: str

    __tablename__ = "categories"


    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text)

    tasks = relationship("TasksModel", secondary=tasks_categories, backref="categories" )
