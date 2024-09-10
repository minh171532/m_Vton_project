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
        query_result = db.query(Cart).filter_by(id=id).all()
        return DbOpStatus.SUCCESS, query_result
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)
    
def read_cart_by_userId_itemId_color_size_status(db, 
                                                  user_id, 
                                                  item_id, 
                                                  color, 
                                                  size, 
                                                  status): 
    """
    """
    try:
        query_result = db.query(
            Cart
        ).filter(
            user_id == user_id,
            item_id == item_id,
            color == color,
            size == size,
            status == status 
        ).first()
        return DbOpStatus.SUCCESS, query_result
        
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        print(traceback.format_exc())
        return DbOpStatus.FAIL, str(e)

def read_carts_by_userId_status(db, user_id, status): 
    try:
        query_result = db.query(Cart).filter(user_id == user_id,
                                             status == status 
                                            ).all()
        return DbOpStatus.SUCCESS, query_result
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        print(traceback.format_exc())
        return DbOpStatus.FAIL, str(e)

def update_cart_quantity(db, id, quantity):
    """
        TODO
    """
    try:
        selected_cart = db.query(Cart).filter_by(id=id).first()
        selected_cart.quantity = quantity
        db.commit()
        return DbOpStatus.SUCCESS, None

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)
    
def update_cart_status(db, user_id, status):
    """
        TODO
    """
    try:
        selected_carts = db.query(Cart).filter_by(user_id=user_id).all()
        for selected_cart in selected_carts:
            selected_cart.status = status
        db.commit()
        return DbOpStatus.SUCCESS, None

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

def delete_cart_by_id(db, id):
    """
        TODO
    """
    try:
        selected_cart = db.query(Cart).filter_by(id=id).first()
        db.delete(selected_cart)
        db.commit()
        return DbOpStatus.SUCCESS, None

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)

def delete_cart_by_userId_status(db, user_id, status): 
    try:
        selected_carts = db.query(Cart).filter(user_id == user_id,
                                             status == status 
                                            ).all()
        for selected_cart in selected_carts: 
            db.delete(selected_cart)
        db.commit()
        return DbOpStatus.SUCCESS, None
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        print(traceback.format_exc())
        return DbOpStatus.FAIL, str(e)
