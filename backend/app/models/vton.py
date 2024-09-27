from sqlalchemy import Column, Integer, String, DateTime, Enum, func, ForeignKey
from models.base import Base
# from models.enums.vton_mode import VtonMode
import uuid

class Vton(Base):
    __tablename__ = 'vton'

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), index=True, nullable=False)
    # item_store_id = Column(Integer, ForeignKey("item_store.id"), index=True, nullable=False)
    image_folder_dir = Column(String, nullable=False)
    color = Column(String, nullable=False)
    # mode = Column(Enum(VtonMode), nullable=False)
    
    created_at = Column(DateTime, primary_key=False, server_default=func.now())
    updated_at = Column(DateTime, primary_key=False, server_default=func.now(), onupdate=func.current_timestamp())
