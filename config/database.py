# config/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ✅ URL koneksi PostgreSQL kamu
DATABASE_URL = "postgresql://postgres:wFgLecFIvYwDoefVXznrxPXUpKjYsQPL@yamabiko.proxy.rlwy.net:33026/railway"

# ✅ Buat engine dengan konfigurasi anti-timeout
engine = create_engine(
    DATABASE_URL,
    pool_size=10,          # jumlah koneksi utama
    max_overflow=20,       # koneksi cadangan jika sibuk
    pool_timeout=30,       # tunggu maksimal 30 detik
    pool_recycle=1800,     # refresh koneksi setiap 30 menit
    pool_pre_ping=True,    # cek koneksi sebelum dipakai (hindari koneksi mati)
    echo=False             # ubah True kalau mau debug query
)

# ✅ Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False  # hindari invalid session
)

# ✅ Base class untuk ORM models
Base = declarative_base()

# ✅ Dependency helper
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()  # penting! agar koneksi dilepas ke pool
