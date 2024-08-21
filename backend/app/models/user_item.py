from sqlalchemy import Column, Integer, String, DateTime, Enum, func, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.enums.job_status import JobStatus
from models.enums.vton_mode import VtonMode


class UserItem(Base):
    __tablename__ = 'user_items'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, ForeignKey("users.id"), index=True, nullable=False)
    item_id = Column(Integer, ForeignKey("items.id"), index=True, nullable=False)
    item_quantity = Column(Integer, nullable=False)
    status = Column(Enum(JobStatus), nullable=False)
    vton_mode = Column(Enum(VtonMode), nullable=False)
    
    created_at = Column(DateTime, primary_key=False, server_default=func.now())
    updated_at = Column(DateTime, primary_key=False, server_default=func.now(), onupdate=func.current_timestamp())
