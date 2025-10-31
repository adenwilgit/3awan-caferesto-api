from flask import Flask, jsonify
from flask_cors import CORS
from config.database import engine, Base, get_db
from routes.web import web
from models.menu_model import Menu
from sqlalchemy.orm import Session

app = Flask(__name__)
CORS(app)  # ✅ Izinkan akses dari Flutter Web

Base.metadata.create_all(bind=engine)
app.register_blueprint(web)


# Route utama menampilkan data JSON dari tabel menus
@app.route("/")
def index():
    db: Session = next(get_db())
    menus = db.query(Menu).all()
    
    # Ubah data ORM menjadi JSON
    return jsonify([
        {
            "id": m.id,
            "name": m.name,
            "price": float(m.price) if str(m.price).replace('.', '', 1).isdigit() else 0.0,
            "category": m.category,
            "image_url": m.image_url
        }
        for m in menus
    ])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
