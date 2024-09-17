from typing import Optional
from pydantic import BaseModel
from models.enums import CartStatus, Size


class CartPydantic(BaseModel, use_enum_values=True):
    id: Optional[str] = None
    user_id: str 
    item_id: int 
    bill_id: str
    quantity: Optional[int] = 1 
    color: str  
    size: Size
    status: Optional[CartStatus] = CartStatus.CHECKOUT

class CartUser(BaseModel):
    user_id: str 

class CartId(BaseModel): 
    cart_id: str 
    user_id: str 