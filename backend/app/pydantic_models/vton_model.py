from typing import Optional 
from pydantic import BaseModel 

class VtonPydantic(BaseModel, use_enum_values=True): 
    id: Optional[str] = None 
    user_id: str 
    image_folder_dir: str 
    color: str 
    