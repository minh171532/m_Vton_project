import traceback
from models.cart import Cart
from models.user import User
from models.item import Item
from models.vton import Vton
from models.enums import DbOpStatus
from models.crud.const import USERNAME_KEY, EMAIL_KEY, ITEM_IMAGE_DIR_KEY


def create_vton(db, vton: Vton):
    try:
        db.add(vton)
        db.commit()
        db.refresh(vton)
        return DbOpStatus.SUCCESS, vton
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)
