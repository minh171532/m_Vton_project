from sqlalchemy import Column, Integer, String, DateTime, Enum, func, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base

class ItemStore(Base):
    __tablename__ = 'item_store'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image_folder_dir = Column(String, ForeignKey("items.image_folder_dir"), nullable=False)
    color = Column(String, nullable=False)
    s_no = Column(Integer, nullable=False)
    m_no = Column(Integer, nullable=False)
    l_no = Column(Integer, nullable=False)
    xl_no = Column(Integer, nullable=False)
    xxl_no = Column(Integer, nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    fk_vton = relationship("Vton", backref="item_store", cascade="all, delete")