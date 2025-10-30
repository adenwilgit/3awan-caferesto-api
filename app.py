from flask import Flask, jsonify
from config.database import engine, Base, get_db
from routes.web import web
from models.menu_model import Menu
from sqlalchemy.orm import Session

app = Flask(__name__)

# Buat tabel otomatis jika belum ada
Base.metadata.create_all(bind=engine)

# Daftarkan route dari file web.py (CRUD endpoint)
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
