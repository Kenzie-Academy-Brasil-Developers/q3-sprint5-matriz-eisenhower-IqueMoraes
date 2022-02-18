from flask import Blueprint, Flask
from app.routes.categories_route import bp_get_all ,bp as bp_categories
from app.routes.tasks_route import bp as bp_tasks


def init_app(app: Flask):

    app.register_blueprint(bp_categories)
    app.register_blueprint(bp_tasks)
    app.register_blueprint(bp_get_all)

    