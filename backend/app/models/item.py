import uuid 
from sqlalchemy import Column, Integer, String, DateTime, Enum, func, ForeignKey, Float
from sqlalchemy.orm import relationship
from models.base import Base
from models.enums.sex import Sex 
from models.enums.category import Category

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sex = Column(Enum(Sex), nullable=False)
    category = Column(Enum(Category), nullable=False)

    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    image_folder_dir = Column(String, nullable=False, unique=True)

    fk_item = relationship("UserItem", backref="items", cascade="all, delete")
