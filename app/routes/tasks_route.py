from app.controllers.tasks_controller import create_task, del_task, update_task
from flask import Blueprint


bp = Blueprint("tasks", __name__, url_prefix="/tasks")

bp.post("")(create_task)
bp.patch("/<int:id>")(update_task)
bp.delete("/<int:id>")(del_task)