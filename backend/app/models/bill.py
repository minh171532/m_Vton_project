from sqlalchemy import Column, Integer, Float, String, DateTime, Enum, func, ForeignKey
from models.base import Base

class Bill(Base):
    __tablename__ = 'bills'

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    location = Column(String)
    total_price = Column(Float)

    created_at = Column(DateTime, primary_key=False, server_default=func.now())
    updated_at = Column(DateTime, primary_key=False, server_default=func.now(), onupdate=func.current_timestamp())
