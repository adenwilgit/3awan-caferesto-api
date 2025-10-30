from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ganti URL ini dengan PostgreSQL URL dari Railway kamu
DATABASE_URL = "postgresql://postgres:wFgLecFIvYwDoefVXznrxPXUpKjYsQPL@yamabiko.proxy.rlwy.net:33026/railway"

# Buat koneksi ke database
engine = create_engine(DATABASE_URL, echo=True)

# Session untuk query
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base untuk model ORM
Base = declarative_base()

# Dependency untuk mendapatkan session database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
