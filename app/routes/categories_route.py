from flask import Blueprint
from app.controllers.categories_controller import create_category, del_category, show_categories, update_category


bp = Blueprint("categories", __name__, url_prefix="/categories")


bp.post("")(create_category)
bp.patch("/<int:id>")(update_category)
bp.delete("/<int:id>")(del_category)

bp_get_all = Blueprint("all categories", __name__)

bp_get_all.get("/")(show_categories)
