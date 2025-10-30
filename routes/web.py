from flask import Blueprint
from controllers.MenuController import (
    get_all_menus, get_menu_by_id, add_menu, update_menu, delete_menu
)

web = Blueprint("web", __name__)

# Endpoint API
web.route("/api/menus", methods=["GET"])(get_all_menus)
web.route("/api/menus/<int:id>", methods=["GET"])(get_menu_by_id)
web.route("/api/menus", methods=["POST"])(add_menu)
web.route("/api/menus/<int:id>", methods=["PUT"])(update_menu)
web.route("/api/menus/<int:id>", methods=["DELETE"])(delete_menu)
