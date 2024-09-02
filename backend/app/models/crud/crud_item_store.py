from fastapi.responses import FileResponse
from models.item import Item
from models.item_store import ItemStore
from models.enums import DbOpStatus


def create_item_store(db, item_store: ItemStore):
    try:
        db.add(item_store)
        db.commit()
        db.refresh(item_store)
        return DbOpStatus.SUCCESS, item_store 
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

# def read_all_item_store(db):
#     try:
#         query_result = db.query(ItemStore).all()
#         return DbOpStatus.SUCCESS, query_result
#     except Exception as e:
#         db.rollback()  # Rollback on error
#         print(f"An error occurred: {e}")
#         return DbOpStatus.FAIL, str(e)
    
def read_item_store_by_image_folder_dir(db, image_folder_dir): 
    try:
        query_result = db.query(ItemStore).filter_by(image_folder_dir=image_folder_dir).all()
        # query_result = query_result.__dict__ 
        return DbOpStatus.SUCCESS, query_result
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)


