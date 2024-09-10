import os
import traceback
from fastapi import status as http_status
from config import CONFIG, LOGGER
from app.utils.app_exceptions import AppExceptionCase
from app.utils.service_result import ServiceResult
from app.database import SessionLocal
from models import crud
from models.enums import DbOpStatus, Sex, Category
from models.crud.const import ITEM_IMAGE_DIR_KEY
from models.item import Item
from pydantic_models.item_model import ItemPydantic

db = SessionLocal()
items_path = CONFIG.ITEM_DIR 

def create_new_vton(): 
    pass 
