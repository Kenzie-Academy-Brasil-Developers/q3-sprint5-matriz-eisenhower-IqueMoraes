from flask import request
from app.models.categories_model import CategoriesModel
from app.models.tasks_model import TasksModel


def create_task():
    data = request.get_json()

    tasks = TasksModel(**data)
    for values in data['categories']:
        category = CategoriesModel.query.filter_by(name = values.capitalize()).one_or_none()
        if category:
            tasks.categories.append(category)

    return "", 201


def update_task(id: int):
    return ""

def del_task(id: int):
    return ""

