import base64
from fastapi.responses import FileResponse
from models.item import Item
from models.item_store import ItemStore
from models.enums import DbOpStatus


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
        query_result = db.query(Item).all()
        return DbOpStatus.SUCCESS, query_result
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

# def read_item_by_id(db,id):
#     try:
#         query_result = db.query(Item).filter_by(id=id).first()
#         return DbOpStatus.SUCCESS, query_result
#     except Exception as e:
#         db.rollback()  # Rollback on error
#         print(f"An error occurred: {e}")
#         return DbOpStatus.FAIL, str(e)
    
def read_item_by_id(db,id):
    """
        TODO 
    """
    try:
        query_result = db.query(Item).filter_by(id=id).first()
        query_item = query_item.__dict__
        return DbOpStatus.SUCCESS, query_result
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)



def read_item_by_sex(db, sex): 
    try:
        query_result = db.query(Item).filter_by(sex=sex).all()
        return DbOpStatus.SUCCESS, query_result
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

def read_item_by_sex_and_category(db, sex, category): 
    try:
        query_result = db.query(Item).filter_by(sex=sex, category=category).all()
        return DbOpStatus.SUCCESS, query_result

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
