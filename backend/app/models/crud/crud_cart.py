import traceback
from models.cart import Cart
from models.user import User
from models.item import Item
from models.enums import DbOpStatus
from models.crud.const import USERNAME_KEY, EMAIL_KEY, ITEM_IMAGE_DIR_KEY


def create_cart(db, cart: Cart):
    try:
        db.add(cart)
        db.commit()
        db.refresh(cart)
        return DbOpStatus.SUCCESS, cart
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)


def read_all_carts(db):
    try:
        query_result = db.query(
            Cart,
            User,
            Item
        ).filter(
            Cart.user_id == User.id,
            Cart.item_id == Item.id
        ).all()
        total_res = []
        for (cart, user_ob, item_ob) in query_result:
            res = cart.__dict__
            res[USERNAME_KEY] = user_ob.__dict__.get(USERNAME_KEY)
            res[EMAIL_KEY] = user_ob.__dict__.get(EMAIL_KEY)
            res[ITEM_IMAGE_DIR_KEY] = item_ob.__dict__.get(ITEM_IMAGE_DIR_KEY)
    
            total_res.append(res)
        return DbOpStatus.SUCCESS, total_res
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        print(traceback.format_exc())
        return DbOpStatus.FAIL, str(e)

def read_all_carts_by_id(db, id): 
    """
        TODO 
    """
    try:
        query_result = db.query(Cart).filter_by(id=id).first()
        return DbOpStatus.SUCCESS, query_result
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

def update_user_item_vton_mode(db, id, vton_mode):
    """
        TODO
    """
    try:
        selected_job = db.query(UserItem).filter_by(id=id).first()
        selected_job.vton_mode = vton_mode
        db.commit()
        return DbOpStatus.SUCCESS, None

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

def delete_carts(db, id):
    """
        TODO
    """
    try:
        selected_job = db.query(UserItem).filter_by(id=id).first()
        db.delete(selected_job)
        db.commit()
        return DbOpStatus.SUCCESS, None

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

# def read_users_items_by_user_id(db, user_id):
#     try:
#         query_result = db.query(UserItem).filter_by(user_id=user_id).all()
#         total_res = []
#         for data_obj in query_result:
#             res = data_obj.__dict__
#             total_res.append(res)
#         return DbOpStatus.SUCCESS, total_res

#     except Exception as e:
#         db.rollback()  # Rollback on error
#         print(f"An error occurred: {e}")
#         return DbOpStatus.FAIL, str(e)

# def read_user_item_by_id(db,id):
#     try:
#         return DbOpStatus.SUCCESS, db.query(UserItem).filter_by(id=id).first()
#     except Exception as e:
#         db.rollback()  # Rollback on error
#         print(f"An error occurred: {e}")
#         return DbOpStatus.FAIL, str(e)

# def update_user_item_status(db, id, status):
#     try:
#         selected_job = db.query(UserItem).filter_by(id=id).first()
#         selected_job.status = status
#         db.commit()
#         return DbOpStatus.SUCCESS, None

#     except Exception as e:
#         db.rollback()  # Rollback on error
#         print(f"An error occurred: {e}")
#         return DbOpStatus.FAIL, str(e)

# def update_user_item_vton_mode(db, id, vton_mode):
#     try:
#         selected_job = db.query(UserItem).filter_by(id=id).first()
#         selected_job.vton_mode = vton_mode
#         db.commit()
#         return DbOpStatus.SUCCESS, None

#     except Exception as e:
#         db.rollback()  # Rollback on error
#         print(f"An error occurred: {e}")
#         return DbOpStatus.FAIL, str(e)

# def delete_user_item(db, id):
#     try:
#         selected_job = db.query(UserItem).filter_by(id=id).first()
#         db.delete(selected_job)
#         db.commit()
#         return DbOpStatus.SUCCESS, None

#     except Exception as e:
#         db.rollback()  # Rollback on error
#         print(f"An error occurred: {e}")
#         return DbOpStatus.FAIL, str(e)
