from typing import Optional
from pydantic import BaseModel
from models.enums import BillStatus


class BillPydantic(BaseModel, use_enum_values=True):
    id: str
    name: Optional[str] = None
    phone_number: Optional[str] = None
    location: Optional[str] = None
    total_price: float 

    bill_status: BillStatus 