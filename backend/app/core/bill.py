import os
import traceback
from fastapi import status as http_status
from config import CONFIG, LOGGER
from app.utils.app_exceptions import AppExceptionCase
from app.utils.service_result import ServiceResult
from app.database import SessionLocal
from models import crud
from models.bill import Bill 
from models.enums import DbOpStatus, BillStatus, Size
from pydantic_models import BillPydantic

db = SessionLocal()

def read_bills(): 
    pass 

def read_bill_by_id():
    pass 

def read_bill_by_billStatus(): 
    pass    

def update_bill_status_by_id(): 
    pass 

def create_new_bill(bill_pydantic: BillPydantic): 
    try: 
        bill_ob = Bill(
        id=bill_pydantic.id,
        name=bill_pydantic.name,
        phone_number=bill_pydantic.phone_number,
        location=bill_pydantic.location,
        total_price=bill_pydantic.total_price,
        
        status=BillStatus(bill_pydantic.bill_status)
        )
        status, data = crud.create_cart(db, bill_ob)
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
