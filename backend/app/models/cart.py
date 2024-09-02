from sqlalchemy import Column, Integer, String, DateTime, Enum, func, ForeignKey
from sqlalchemy.orm import relationship
from models.base import Base
from models.enums.cart_status import CartStatus
from models.enums.size import Size 


class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    item_id = Column(Integer, ForeignKey("items.id"), index=True, nullable=False)
    user_id = Column(String, ForeignKey("users.id"), index=True, nullable=False)
    bill_id = Column(String, nullable=False)

    quantity = Column(Integer, nullable=False)
    size = Column(Enum(Size), nullable=False)
    status = Column(Enum(CartStatus), nullable=False)
    
    created_at = Column(DateTime, primary_key=False, server_default=func.now())
    updated_at = Column(DateTime, primary_key=False, server_default=func.now(), onupdate=func.current_timestamp())

    # fk_bills = relationship("Bill", backref="carts", cascade="all, delete")
