from typing import Optional
from pydantic import BaseModel
from models.enums import Sex, Category

class ItemPydantic(BaseModel, use_enum_values=True):
    id: Optional[int] = None
    sex: Sex
    category: Category
    title: str
    description: str
    price: float
    image_folder_dir:str 

    