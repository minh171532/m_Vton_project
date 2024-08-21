from models.item import Item
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
