from typing import Optional
from pydantic import BaseModel


class ItemPydantic(BaseModel, use_enum_values=True):
    id: Optional[int] = None
    tag: str
    image_dir:str 
    mask_dir:str
    