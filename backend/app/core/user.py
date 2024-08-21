import traceback
from fastapi import status as http_status
from config import LOGGER
from app.utils.app_exceptions import AppExceptionCase
from app.utils.service_result import ServiceResult
from app.database import SessionLocal
from models import crud
from models.enums import DbOpStatus, UserRoles
from models.user import User
from pydantic_models.user_model import UserPydantic

db = SessionLocal()

HASHED_PASSWORD_KEY = "hashed_password"


def remove_hashed_password_key(dict):
    if HASHED_PASSWORD_KEY in dict:
        dict.pop(HASHED_PASSWORD_KEY)
    return dict


def read_all_users():
    try:
        status, data = crud.read_all_users(db)
        if status == DbOpStatus.SUCCESS:
            res = []
            for data_obj in data:
                data_dict = data_obj.__dict__
                data_dict = remove_hashed_password_key(data_dict)
                res.append(data_dict)
            return ServiceResult(res)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))


def read_user_by_username(username):
    try:
        status, data = crud.read_one_user(db, username)
        if status == DbOpStatus.SUCCESS:
            data_dict = data.__dict__
            data_dict = remove_hashed_password_key(data_dict)
            return ServiceResult(data_dict)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))


def create_new_user(user_pydantic: UserPydantic):
    try:
        user_ob = User(
            username=user_pydantic.username,
            email=user_pydantic.email,
            role=UserRoles(user_pydantic.role),
            description=user_pydantic.description,
        )
        user_ob.set_password(user_pydantic.password)
        status, data = crud.create_user(db, user_ob)
        if status == DbOpStatus.SUCCESS:
            data_dict = data.__dict__
            data_dict = remove_hashed_password_key(data_dict)
            return ServiceResult(data_dict)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        print(traceback.format_exc())
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))


def delete_user_by_id(user_id: str):
    try:
        # Delete 
        status, data = crud.delete_user(db, user_id)
        if status == DbOpStatus.SUCCESS:
            return ServiceResult(None)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        print(traceback.format_exc())
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))


def update_user_by_id(user_id: str, user_pydantic: UserPydantic):
    try:
        status, data = crud.update_user(db, user_id=user_id, **user_pydantic.dict())
        if status == DbOpStatus.SUCCESS:
            return ServiceResult(None)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        print(traceback.format_exc())
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))
