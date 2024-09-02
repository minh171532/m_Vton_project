from sqlalchemy import Column, Integer, String, DateTime, Enum, func, ForeignKey
from models.base import Base
from models.enums.vton_mode import VtonMode

class Vton(Base):
    __tablename__ = 'vton'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), index=True, nullable=False)
    item_store_id = Column(Integer, ForeignKey("item_store.id"), index=True, nullable=False)

    mode = Column(Enum(VtonMode), nullable=False)
    
    created_at = Column(DateTime, primary_key=False, server_default=func.now())
    updated_at = Column(DateTime, primary_key=False, server_default=func.now(), onupdate=func.current_timestamp())
