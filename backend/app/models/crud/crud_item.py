import base64

from fastapi.responses import FileResponse
from models.item import Item
from models.enums import DbOpStatus
from models.crud.const import ITEM_IMAGE_DIR_KEY

def create_item(db, item: Item):
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
        return DbOpStatus.SUCCESS, item 
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

def read_all_items(db):
    try:
        return DbOpStatus.SUCCESS, db.query(Item).all()
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

def read_item_by_id(db,id):
    try:
        return DbOpStatus.SUCCESS, db.query(Item).filter_by(id=id).first()
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)
    
def read_item_by_sex(db, sex): 
    try:
        query_result = db.query(Item).filter_by(sex=sex).all()
        total_res = []
        for data_obj in query_result:
            res = data_obj.__dict__
            res_ = dict()
            res_["_id"] = res["id"]
            res_["title"] = "abc"
            res_["price"] = 22
            res_["description"] = "abcdef"
            res_["category"] = res["cloth_type"]
            res_["image"] = f"http://192.168.0.105:5111/images/{res[ITEM_IMAGE_DIR_KEY]}"
            res_["__v"] = 0 
            total_res.append(res_)
        return DbOpStatus.SUCCESS, total_res

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

def read_item_by_sex_and_cloth_type(db, sex, cloth_type): 
    try:
        query_result = db.query(Item).filter_by(sex=sex, cloth_type=cloth_type).all()
        total_res = []
        for data_obj in query_result:
            res = data_obj.__dict__
            total_res.append(res)
        return DbOpStatus.SUCCESS, total_res

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

def delete_item(db, id):
    try:
        selected_job = db.query(Item).filter_by(id=id).first()
        db.delete(selected_job)
        db.commit()
        return DbOpStatus.SUCCESS, None

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)
