from flask import Blueprint
from app.controllers.categories_controller import create_category, del_category, update_category, show_categories


bp = Blueprint("categories", __name__, url_prefix="/")

bp.get("")(show_categories)
bp.post("categories")(create_category)
bp.patch("categories/<int:id>")(update_category)
bp.delete("categories/<int:id>")(del_category)


