from app.configs.database import db
from sqlalchemy import ForeignKey, Integer, Column 


tasks_categories = db.Table('tasks_categories',
    Column('id', Integer, primary_key=True),
    Column('task_id', Integer, ForeignKey('tasks.id')),
    Column('category_id', Integer, ForeignKey('categories.id'))
)



##PARA ESTUDO
# @dataclass
# class TasksCategories(db.Model):
#     id: int
#     task_id: int
#     category_id: int

#     __tablename__ = "tasks_categories"

#     id = Column(Integer, primary_key=True)
#     task_id = Column(Integer, ForeignKey('tasks.id'), nullable=False)
#     category_id = Column(Integer, ForeignKey('categories.id', nullable=False))