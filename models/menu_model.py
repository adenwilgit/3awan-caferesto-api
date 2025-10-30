from sqlalchemy import Column, Integer, String
from config.database import Base

class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(String, nullable=False)  # disimpan sebagai text
    category = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
