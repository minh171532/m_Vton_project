import os
import socket
import traceback
from fastapi import status as http_status
from config import LOGGER
from app.utils.app_exceptions import AppExceptionCase
from app.utils.service_result import ServiceResult
from app.database import SessionLocal
from models import crud
from models.enums import DbOpStatus, Sex, ClothType
from models.item import Item
from pydantic_models.item_model import ItemPydantic

db = SessionLocal()


def read_items():
    try:
        status, data = crud.read_all_items(db)
        if status == DbOpStatus.SUCCESS:
            # convert data to send image 
            return ServiceResult(data)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))

def read_item_by_id(id: int):
    try:
        status, data = crud.read_item_by_id(db, id)
        if status == DbOpStatus.SUCCESS:
            data_dict = data.__dict__
            return ServiceResult(data_dict)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))

def read_item_by_sex(sex: Sex): 
    try:
        status, data = crud.read_item_by_sex(db, sex)
        if status == DbOpStatus.SUCCESS:
            return ServiceResult(data)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))

def read_item_by_sex_and_cloth_type(sex: Sex, cloth_type: ClothType):
    try:
        status, data = crud.read_item_by_sex_and_cloth_type(db, sex, cloth_type)
        if status == DbOpStatus.SUCCESS:
            return ServiceResult(data)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))

def create_new_item(item_pydantic: ItemPydantic):
    # create database from storage 
    try:
        item_ = Item(
            sex= Sex(item_pydantic.sex),
            cloth_type= ClothType(item_pydantic.cloth_type),
            image_dir=item_pydantic.image_dir,
            mask_dir=item_pydantic.mask_dir,
        )
        status, data = crud.create_item(db, item_)
        if status == DbOpStatus.SUCCESS:
            data_dict = data.__dict__
            return ServiceResult(data_dict)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        print(traceback.format_exc())
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))

def delete_item_by_id(id: int):
    try:
        # Delete 
        status, data = crud.delete_item(db, id=id)
        if status == DbOpStatus.SUCCESS:
            return ServiceResult(None)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        print(traceback.format_exc())
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))
