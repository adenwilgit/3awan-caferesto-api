from flask import Flask, jsonify
from flask_cors import CORS
from config.database import engine, Base, SessionLocal
from routes.web import web
from models.menu_model import Menu

app = Flask(__name__)
CORS(app)  # ✅ Izinkan akses dari Flutter Web

# 🔧 Buat tabel otomatis
Base.metadata.create_all(bind=engine)

# 🔗 Register blueprint
app.register_blueprint(web)


# 🌐 Route utama menampilkan semua data menu (dengan koneksi otomatis tertutup)
@app.route("/")
def index():
    with SessionLocal() as db:  # ✅ Koneksi otomatis ditutup setelah selesai
        menus = db.query(Menu).all()
        return jsonify([
            {
                "id": m.id,
                "name": m.name,
                "price": float(m.price),
                "category": m.category,
                "image_url": m.image_url
            }
            for m in menus
        ])


if __name__ == "__main__":
    # 🚀 Jalankan server
    app.run(debug=True, host="0.0.0.0", port=5000)
