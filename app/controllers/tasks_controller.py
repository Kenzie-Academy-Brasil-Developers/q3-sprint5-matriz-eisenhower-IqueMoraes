from flask import current_app, jsonify, request
from app.controllers.tasks_exc import NumerosInvalidos
from app.models.categories_model import CategoriesModel
from app.models.eisenhowers_model import EisenhowersModel
from app.models.tasks_model import TasksModel
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation,NoData


def create_task():
    data = request.get_json()
    
    try:
        data['name'] = data['name'].lower()
        data_categories = data.pop('categories')
        importance = data['importance']
        urgency = data['urgency']
        allowed_values = [1,2]

        if importance not in allowed_values or urgency not in allowed_values:
            raise NumerosInvalidos(description="De acordo com a matriz Einsenhower apenas são permitidos os valores 1 e 2 nas chaves 'urgency' e 'importance'.")

        data['eisenhower_id'] = eisenhower(i=importance, u=urgency)

        task = TasksModel(**data)

        categories_ids = find_categories(data_categories)
        task.categories.extend(categories_ids)

        current_app.db.session.add(task)
        current_app.db.session.commit()


        return {
            "id": task.id,
            "name": task.name,
            "description": task.description,
            "duration": task.duration,
            "classification": EisenhowersModel.query.filter(EisenhowersModel.id == task.eisenhower_id).first().type,
            "categories": [c.name for c in task.categories]
        }, 201



    except NumerosInvalidos as e:
        return {
            "msg": {
                "valid_options": {
                "importance": [1, 2],
                "urgency": [1, 2]
                },
                "recieved_options": {
                "importance": 4,
                "urgency": 1
                }
            }
            }, e.code

    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation ):
            return {"msg": "task already exists!"}, 400




def update_task(id: int):
    data = request.get_json()

    try:
        task = TasksModel.query.filter_by(id=id).one_or_none()
        print(task.importance)
        if 'name' in data.keys():
            data['name'] = data['name'].lower()

        if 'importance' in data.keys():
            if data['importance'] not in [1,2]:
                raise NumerosInvalidos

        if 'urgency' in data.keys():
            if data['urgency'] not in [1,2]:
                raise NumerosInvalidos


        for key, value in data.items():
            if key == 'categories':
                categories_ids = find_categories(data['categories'])
                setattr(task, key, categories_ids)
            else:
                setattr(task, key, value)

        setattr(task, 'eisenhower_id',  eisenhower(i=task.importance, u=task.urgency))

        current_app.db.session.add(task)
        current_app.db.session.commit()

        return {
            "id": task.id,
            "name": task.name,
            "description": task.description,
            "duration": task.duration,
            "classification": EisenhowersModel.query.filter(EisenhowersModel.id == task.eisenhower_id).first().type,
            "categories": [c.name for c in task.categories]
        }, 200



    except NumerosInvalidos as e:
        return {
            "msg": {
                "valid_options": {
                "importance": [1, 2],
                "urgency": [1, 2]
                },
                "recieved_options": {
                "importance": 4,
                "urgency": 1
                }
            }
            }, e.code

    except AttributeError as e:
        return {"msg": "task not found!"}, 404




def del_task(id: int):
    try:
        task = TasksModel.query.filter_by(id = id).one_or_none()

        if not task:
            raise NoData

        current_app.db.session.delete(task)
        current_app.db.session.commit()

        return "", 204

    except NoData:
        return {"msg": "task not found!"}, 404





def show_tasks():

    tasks = TasksModel.query.all()

    print(tasks)

    return [{
            "id": task.id,
            "name": task.name,
            "description": task.description,
            "duration": task.duration,
            "classification": EisenhowersModel.query.filter(EisenhowersModel.id == task.eisenhower_id).first().type,
            "categories": [c.name for c in task.categories]
        } for task in tasks], 200




def eisenhower(*, i, u):
    matriz_id = [[1,1], [1,2], [2,1], [2,2]]

    return matriz_id.index([i, u]) + 1


def find_categories(c_list):

    categories_ids = []

    for values in c_list:
        category = CategoriesModel.query.filter_by(name = values.lower()).one_or_none()
        if category:
            categories_ids.append(category)
        else:
            new_category = CategoriesModel(name=values.lower())
            current_app.db.session.add(new_category)
            current_app.db.session.commit()

            categories_ids.append(new_category)

    return categories_ids

