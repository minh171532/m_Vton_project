import uuid 
from sqlalchemy import Column, Integer, String, DateTime, Enum, func, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.enums.sex import Sex 
from models.enums.cloth_type import ClothType

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sex = Column(Enum(Sex), nullable=False)
    cloth_type = Column(Enum(ClothType), nullable=False)
    image_dir = Column(String, nullable=False, unique=True)
    mask_dir = Column(String, nullable=False, unique=True)

    fk_item = relationship("UserItem", backref="items", cascade="all, delete")
