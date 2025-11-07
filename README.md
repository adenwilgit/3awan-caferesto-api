# ☕ 3awan Cafe & Resto API (Flask Backend)

Backend REST API untuk aplikasi **3awan Cafe & Resto**,
dibangun menggunakan **Flask**, **SQLAlchemy**, dan **PostgreSQL**,
serta dideploy menggunakan **Railway**.

🔗 **Live API URL:** [https://3awan-caferesto-api.up.railway.app](https://3awan-caferesto-api.up.railway.app)

---

## 🚀 Teknologi yang Digunakan

* Python 3.x
* Flask
* SQLAlchemy (ORM)
* PostgreSQL (Database)
* Railway (Deployment)
* Flask-CORS (untuk Flutter Web)

---

## 📁 Struktur Folder

```
3awan-caferesto-api/
│
├── config/
│   └── database.py         # Konfigurasi koneksi PostgreSQL & SQLAlchemy
│
├── controllers/
│   └── MenuController.py   # CRUD logika utama menu
│
├── models/
│   └── menu_model.py       # Model ORM Menu
│
├── routes/
│   └── web.py              # Routing API
│
├── app.py                  # Entry point utama Flask
├── requirements.txt        # Daftar dependencies Python
└── README.md
```

---

## ⚙️ Instalasi & Menjalankan Server Lokal

### 1️⃣ Clone repository

```bash
git clone https://github.com/adenwilgit/3awan-caferesto-api.git
cd 3awan-caferesto-api
```

### 2️⃣ Buat virtual environment

```bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Jalankan server Flask

```bash
python app.py
```

Server akan berjalan di:

> 🔗 `http://127.0.0.1:5000`

---

## 🧩 Endpoint API

| Method | Endpoint          | Deskripsi                 |
| ------ | ----------------- | ------------------------- |
| GET    | `/api/menus`      | Ambil semua menu          |
| GET    | `/api/menus/<id>` | Ambil menu berdasarkan ID |
| POST   | `/api/menus`      | Tambah menu baru          |
| PUT    | `/api/menus/<id>` | Update menu               |
| DELETE | `/api/menus/<id>` | Hapus menu                |

### Contoh Request (POST)

```json
POST /api/menus
{
  "name": "Nasi Goreng Spesial",
  "price": "15000",
  "category": "Makanan",
  "image_url": "https://example.com/nasi-goreng.jpg"
}
```

---

## 🧠 Catatan Penting

⚡ Railway terkadang *sleep mode* jika tidak diakses dalam waktu lama.
Jika API menampilkan `TimeoutError`, buka kembali link:

> [https://3awan-caferesto-api.up.railway.app](https://3awan-caferesto-api.up.railway.app)

untuk “membangunkan” server sebelum digunakan oleh aplikasi Flutter.

---

## 🧰 Deployment di Railway

1. Push kode ke GitHub.
2. Masuk ke [https://railway.app](https://railway.app).
3. Buat proyek baru → *Deploy from GitHub repository*.
4. Pilih repo `3awan-caferesto-api`.
5. Tambahkan variabel `DATABASE_URL` dari PostgreSQL Railway.
6. Deploy otomatis — URL API akan aktif seperti contoh di atas.

---

## ✨ Author

**Aden Wilgit**
📧 Email: *(isi dengan emailmu)*
🔗 Repo: [https://github.com/adenwilgit/3awan-caferesto-api](https://github.com/adenwilgit/3awan-caferesto-api)
🚀 API: [https://3awan-caferesto-api.up.railway.app](https://3awan-caferesto-api.up.railway.app)
