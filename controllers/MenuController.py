from flask import jsonify, request
from config.database import get_db
from models.menu_model import Menu
from sqlalchemy.orm import Session

# GET all menus
def get_all_menus():
    db: Session = next(get_db())
    menus = db.query(Menu).all()
    return jsonify([{
        "id": m.id,
        "name": m.name,
        "price": float(m.price) if m.price.replace('.', '', 1).isdigit() else 0.0,
        "category": m.category,
        "image_url": m.image_url
    } for m in menus])

# GET menu by ID
def get_menu_by_id(id):
    db: Session = next(get_db())
    menu = db.query(Menu).filter(Menu.id == id).first()
    if not menu:
        return jsonify({"message": "Menu not found"}), 404
    return jsonify({
        "id": menu.id,
        "name": menu.name,
        "price": float(menu.price) if menu.price.replace('.', '', 1).isdigit() else 0.0,
        "category": menu.category,
        "image_url": menu.image_url
    })

# POST add menu
def add_menu():
    db: Session = next(get_db())
    body = request.json

    new_menu = Menu(
        name=body["name"],
        price=str(body["price"]),  # disimpan sebagai teks
        category=body["category"],
        image_url=body["image_url"]
    )

    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)

    return jsonify({"message": "Menu added", "id": new_menu.id})

# PUT update menu
def update_menu(id):
    db: Session = next(get_db())
    body = request.json
    menu = db.query(Menu).filter(Menu.id == id).first()

    if not menu:
        return jsonify({"message": "Menu not found"}), 404

    menu.name = body["name"]
    menu.price = str(body["price"])
    menu.category = body["category"]
    menu.image_url = body["image_url"]

    db.commit()
    return jsonify({"message": "Menu updated"})

# DELETE menu
def delete_menu(id):
    db: Session = next(get_db())
    menu = db.query(Menu).filter(Menu.id == id).first()

    if not menu:
        return jsonify({"message": "Menu not found"}), 404

    db.delete(menu)
    db.commit()
    return jsonify({"message": "Menu deleted"})
