from typing import Optional
from pydantic import BaseModel
from models.enums import Sex, ClothType

class ItemPydantic(BaseModel, use_enum_values=True):
    id: Optional[int] = None
    sex: Sex
    cloth_type: ClothType
    image_dir:str 
    mask_dir:str
    