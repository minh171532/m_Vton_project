from typing import Optional
from pydantic import BaseModel
from models.enums import UserRoles


class UserPydantic(BaseModel, use_enum_values=True):
    id: Optional[str] = None
    username: str
    password: str
    email: Optional[str] = None
    role: UserRoles
    setting_path: str
    description: Optional[str] = None
