import os
import socket
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


def read_items():
    """
        total_res = [{
                    _id : int,
                    title: srt,
                    price: float, 
                    description: str, 
                    category: str
                    colors = {
                        red_dir : 
                        blu_dir : 
            }
        },
        {}
        ]
    """
    try:
        status, query_result = crud.read_all_items(db)
        if status == DbOpStatus.SUCCESS:
            total_res = []
            for data_obj in query_result:
                res = data_obj.__dict__
                res_ = dict()

                res_["_id"] = res["id"]
                res_["title"] = res["title"]
                res_["price"] = res["price"]
                res_["description"] = res["description"]
                res_["category"] = res["category"]

                res_["colors"] = {}
                item_dir = os.path.join(items_path, res[ITEM_IMAGE_DIR_KEY])
                colors = os.listdir(item_dir)

                # TODO 
                for color in colors: 
                    res_["colors"][color] = os.path.join("http://192.168.0.105:5111/images/",
                                                        res[ITEM_IMAGE_DIR_KEY], color, "1.png")
                    
                # res_["image"] = f"http://192.168.0.105:5111/images/{res[ITEM_IMAGE_DIR_KEY]}"
                res_["__v"] = 0 
                total_res.append(res_)

            return ServiceResult(total_res)
        else:
            LOGGER.error("DB Exception: {}".format(query_result))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                                  context=query_result))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                              context=str(e)))


def read_item_by_id(id: int):
    """
        res_ = {
            _id : int,
            title: srt,
            price: float, 
            description: str, 
            category: str
            colors = {
                red : {
                    img_dir = str,
                    image_list: [],
                    item_store_id: int,
                    s_no: int,
                    m_no: int,
                    l_no: int,
                    xl_no: int,
                    xxl_no: int
                },
                blu : {}
            }
        }
    """
    try:
        status, query_result = crud.read_item_by_id(db, id)
        if status == DbOpStatus.SUCCESS:

            res = query_result.__dict__ 
            res_ = {}
            res_["_id"] = res["id"]
            res_["title"] = res["title"]
            res_["price"] = res["price"]
            res_["description"] = res["description"]
            res_["category"] = res["category"]

            _, query_itemstore_list = crud.read_item_store_by_image_folder_dir(db,
                                                                          image_folder_dir=res["image_folder_dir"])
            # ===================
            res_["colors"] = {}
            item_dir = os.path.join(items_path, res[ITEM_IMAGE_DIR_KEY])
            for query_itemstore in query_itemstore_list: 
                query_itemstore = query_itemstore.__dict__ 
                color = query_itemstore["color"]

                res_["colors"][color] = {}
                res_["colors"][color]["img_dir"] = os.path.join("http://192.168.0.105:5111/images/",
                                                                res[ITEM_IMAGE_DIR_KEY], color, "1.png")
                res_["colors"][color]["item_store_id"] = query_itemstore["id"]
                res_["colors"][color]["s_no"] = query_itemstore["s_no"]
                res_["colors"][color]["m_no"] = query_itemstore["m_no"]
                res_["colors"][color]["l_no"] = query_itemstore["l_no"]
                res_["colors"][color]["xl_no"] = query_itemstore["xl_no"]
                res_["colors"][color]["xxl_no"] = query_itemstore["xxl_no"]
                res_["colors"][color]["image_list"] = []

                color_dir = os.path.join(item_dir, color)
                img_names = os.listdir(color_dir)

                for img_name in img_names: 
                    res_["colors"][color]["image_list"] .append(os.path.join("http://192.168.0.105:5111/images/",
                                                            res[ITEM_IMAGE_DIR_KEY], color, img_name))
            res_["__v"] = 0 

            return ServiceResult(res_)
        else:
            LOGGER.error("DB Exception: {}".format(query_result))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                                  context=query_result))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                              context=str(e)))

def read_item_by_sex(sex: Sex): 
    """
        total_res = [{
                    _id : int,
                    title: srt,
                    price: float, 
                    description: str, 
                    category: str
                    colors = {
                        red_dir : 
                        blu_dir : 
            }
        },
        {}
        ]
    """
    try:
        status, query_result = crud.read_item_by_sex(db, sex)
        if status == DbOpStatus.SUCCESS:
            total_res = []
            for data_obj in query_result:
                res = data_obj.__dict__
                res_ = dict()
                res_["_id"] = res["id"]
                res_["title"] = res["title"]
                res_["price"] = res["price"]
                res_["description"] = res["description"]
                res_["category"] = res["category"]

                res_["colors"] = {}
                item_dir = os.path.join(items_path, res[ITEM_IMAGE_DIR_KEY])
                colors = os.listdir(item_dir)

                for color in colors: 
                    res_["colors"][color] = os.path.join("http://192.168.0.105:5111/images/",
                                                        res[ITEM_IMAGE_DIR_KEY], color, "1.png")
                    
                res_["__v"] = 0 
                total_res.append(res_)

            return ServiceResult(total_res)
        else:
            LOGGER.error("DB Exception: {}".format(query_result))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                                  context=query_result))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))

def read_item_by_sex_and_category(sex: Sex, category: Category):
    """
        total_res = [{
                    _id : int,
                    title: srt,
                    price: float, 
                    description: str, 
                    category: str
                    colors = {
                        red_dir : 
                        blu_dir : 
            }
        },
        {}
        ]
    """
    try:
        status, query_result = crud.read_item_by_sex_and_category(db, sex, category)
        if status == DbOpStatus.SUCCESS:
            total_res = []
            for data_obj in query_result:
                res = data_obj.__dict__
                res_ = dict()
                res_["_id"] = res["id"]
                res_["title"] = res["title"]
                res_["price"] = res["price"]
                res_["description"] = res["description"]
                res_["category"] = res["category"]

                res_["colors"] = {}
                item_dir = os.path.join(items_path, res[ITEM_IMAGE_DIR_KEY])
                colors = os.listdir(item_dir)

                for color in colors: 
                    res_["colors"][color] = os.path.join("http://192.168.0.105:5111/images/",
                                                        res[ITEM_IMAGE_DIR_KEY], color, "1.png")
                    
                res_["__v"] = 0 
                total_res.append(res_)



            return ServiceResult(total_res)
        else:
            LOGGER.error("DB Exception: {}".format(query_result))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                                  context=query_result))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))

def create_new_item(item_pydantic: ItemPydantic):
    # create database from storage 
    try:
        item_ = Item(
            sex= Sex(item_pydantic.sex),
            category= Category(item_pydantic.category),
            title=item_pydantic.title,
            description=item_pydantic.description,
            price=item_pydantic.price,
            image_folder_dir=item_pydantic.image_folder_dir

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
