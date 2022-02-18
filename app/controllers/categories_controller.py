
from unicodedata import category
from xml.etree.ElementInclude import include
from flask import request, current_app, jsonify
from app.models.categories_model import CategoriesModel
from app.configs.database import db
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import UnmappedInstanceError
from psycopg2.errors import UniqueViolation


def create_category():
    data = request.get_json()
    
    try:
        session = current_app.db.session

        data['name'] = data['name'].capitalize()

        category = CategoriesModel(**data)
        session.add(category)
        session.commit()

        return jsonify(category), 201
    
    except IntegrityError as e:
        if isinstance(e.orig, UniqueViolation):
            return { "msg": "category already exists!"}, 409


def update_category(id: int):
    data = request.get_json()

    try:
        session = current_app.db.session

        category = CategoriesModel.query.filter_by(id=id).one_or_none()

        for key, value in data.items():
            setattr(category, key, value)

        session.add(category)
        session.commit()

        return jsonify(category),200
    
    except AttributeError:
        return { "msg": "category not found!"}, 404


def del_category(id: int):
    try:
        category = CategoriesModel.query.filter_by(id=id).one_or_none()
        current_app.db.session.delete(category)
        current_app.db.session.commit()

        return "", 204

    except UnmappedInstanceError:
        return { "msg": "category not found!"}, 404


def show_categories():
    return ""
