import uuid
from sqlalchemy import Column, Integer, String, DateTime, Enum, func
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types.email import EmailType
import bcrypt

from models.base import Base
from .enums.user_roles import UserRoles


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, nullable=False, index=True, unique=True)
    hashed_password = Column(String, nullable=False)
    email = Column(EmailType, nullable=True, unique=True)
    role = Column(Enum(UserRoles), nullable=False)

    description = Column(String, nullable=True)

    def set_password(self, password: str):
        self.hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.hashed_password.encode('utf-8'))

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.current_timestamp())

    fk_carts = relationship("Cart", backref="users", cascade="all, delete")
    fk_vton = relationship("Vton", backref="users", cascade="all, delete")
