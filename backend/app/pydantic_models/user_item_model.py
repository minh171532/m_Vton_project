from typing import Optional
from pydantic import BaseModel
from models.enums import JobStatus, VtonMode


class UserItemPydantic(BaseModel, use_enum_values=True):
    id: Optional[int] = None
    user_id: str 
    item_id: str 
    item_quantity: int 
    status: Optional[JobStatus] = JobStatus.WAITING
    vton_mode: VtonMode

