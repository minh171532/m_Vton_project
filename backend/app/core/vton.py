import os
import traceback
import shutil 
from typing import List

from fastapi import status as http_status, UploadFile, File
from config import CONFIG, LOGGER
from app.producer import RpcClient 

from app.utils.app_exceptions import AppExceptionCase
from app.utils.service_result import ServiceResult
from app.database import SessionLocal
from models import crud
from models.enums import DbOpStatus, Sex, Category
from models.crud.const import ITEM_IMAGE_DIR_KEY
from models.vton import Vton 
from pydantic_models.vton_model import VtonPydantic 

db = SessionLocal()
human_image_path = CONFIG.HUMAN_IMAGE_DIR
mask_image_path = CONFIG.MASK_IMAGE_DIR

rpc_client = RpcClient()

# def add_new_vton(vton_pydantic: VtonPydantic,  files: List[UploadFile] = File(...)): 
def add_new_vton(vton_pydantic: VtonPydantic,  files: List[UploadFile]): 
    """
        add vton to db and, save human_image, mask_image.  
        return result image dir. 
    """
    try: 
        vton_ob = Vton(
            user_id= vton_pydantic.user_id,
            image_folder_dir=vton_pydantic.image_folder_dir,
            color=vton_pydantic.color 
        )
        status, data = crud.create_vton(db, vton_ob)
        if status == DbOpStatus.SUCCESS:
            # save human_image, mask_image 
            image_name = vton_pydantic.user_id + ".png"
            with open(os.path.join(human_image_path, image_name), "wb") as buffer:
                shutil.copyfileobj(files[0].file, buffer)
            with open(os.path.join(mask_image_path, image_name), "wb") as buffer:
                shutil.copyfileobj(files[1].file, buffer)
            
            a = {"oke":"oke"}
            return a 
            # # call rabbit mq 
            # massage = "{},{},{}".format(vton_pydantic.user_id,vton_pydantic.image_folder_dir,vton_pydantic.color)
            # response = rpc_client.call(massage)
            # if response: 
            #     # response to UI  
            #     result = {}
            #     # result["result_image"] = os.path.join("http://localhost:5111/images/",
            #     #                                             res[ITEM_IMAGE_DIR_KEY], color, "1.png")
            #     return ServiceResult(result)
            # else: 
            #     LOGGER.error("Exception: {}".format(e))
            #     print(traceback.format_exc())
            #     return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))

        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                                  context=data))
    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        print(traceback.format_exc())
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))
