import os
import traceback
import uuid 
from fastapi import status as http_status
from config import CONFIG, LOGGER
from app.utils.app_exceptions import AppExceptionCase
from app.utils.service_result import ServiceResult
from app.database import SessionLocal
from models import crud
from models.cart import Cart
from models.bill import Bill 
from models.crud.const import ITEM_IMAGE_DIR_KEY
from models.enums import DbOpStatus, CartStatus, Size
from pydantic_models.cart_module import CartPydantic


db = SessionLocal()

def add_to_cart(cart_pydantic: CartPydantic): 
    """
    {
    _id: (bill_id)
    count: int 
    products: [{},{
        create_at: dateTime 
        quantity: int
        color: str #  
        size: #   
        _id: (item_id)
        product_id: {
            category: str,
            description: str,
            image: url, 
            price: float, 
            title: 
            _id: (cart_id)
            }   
        }]
    }
    """
    try: 
        #  Check exist cart by userId, itemId color size Status. (TODO)
        _, query_result = crud.read_cart_by_userId_itemId_color_size_status(db, user_id=cart_pydantic.user_id, 
                                                                                 item_id=cart_pydantic.item_id,
                                                                                 color=cart_pydantic.color,
                                                                                 size=cart_pydantic.size,
                                                                                 status=CartStatus.CHECKOUT)
        if query_result: 
            # Update cart (increment)
            update_quantity = query_result.quantity + 1
            crud.update_cart_quantity(db, id=query_result.id, quantity=update_quantity)
        else: 
            _, query_result = crud.read_carts_by_userId_status(db, 
                                                               user_id=cart_pydantic.user_id, 
                                                               status=CartStatus.CHECKOUT)
            if query_result: 
                # Create cart (add to cart)
                cart_ob=Cart(item_id=cart_pydantic.item_id,
                             user_id=cart_pydantic.user_id,
                             bill_id=query_result[0].bill_id,
                             color=cart_pydantic.color,
                             quantity=cart_pydantic.quantity,
                             size=Size(cart_pydantic.size), 
                             status=CartStatus.CHECKOUT
                )
                crud.create_cart(db, cart_ob)
            else: 
                # Create bill 
                # Create cart 

                bill_db = Bill(
                    id = str(uuid.uuid4()),
                    name = "temp",
                    phone_number = "temp",
                    location="temp",
                    total_price = 0 
                )                
                crud.create_bill(db, bill_db)
                print(">>> cart_pydantic  ", cart_pydantic.color)
                cart_ob=Cart(item_id=cart_pydantic.item_id,
                             user_id=cart_pydantic.user_id,
                             bill_id=bill_db.id,
                             color=cart_pydantic.color,
                             quantity=cart_pydantic.quantity,
                             size=Size(cart_pydantic.size), 
                             status=CartStatus.CHECKOUT
                )
                crud.create_cart(db, cart_ob)

        # response 
        status, query_results = crud.read_carts_by_userId_status(db, 
                                                    user_id=cart_pydantic.user_id, 
                                                    status=CartStatus.CHECKOUT)
        
        if status == DbOpStatus.SUCCESS:
            response = {}
            count = 0 
            response["_id"] = query_results[0].bill_id 
            response["products"] = []

            for query_result in query_results: 
                query_result = query_result.__dict__ 
                count += query_result["quantity"]
                product = {}
                product["create_at"] = query_result["created_at"]
                product["quantity"] = query_result["quantity"]
                product["color"] = query_result["color"]
                product["size"] = query_result["size"]
                product["_id"] = query_result["item_id"]
                product["product_id"] = {}
                # 
                _, item = crud.read_item_by_id(db, id=query_result["item_id"])
                item = item.__dict__ 
                product["product_id"]["category"] = item["category"]
                product["product_id"]["description"] = item["description"]
                product["product_id"]["image"] = os.path.join("http://localhost:5111/images/",
                                                                item[ITEM_IMAGE_DIR_KEY], query_result["color"], "1.png")

                product["product_id"]["price"] = item["price"]
                product["product_id"]["title"] = item["title"]
                product["product_id"]["_id"] = query_result["id"]

                response["products"].append(product)

            response["count"] = count 
            return ServiceResult(response)
        else:
            LOGGER.error("DB Exception: {}".format(query_results))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=query_results))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        print(traceback.format_exc())
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))

# def read_cart_by_userId_itemId_status(db, user_id: str, item_id : int, status: CartStatus): 
#     try: 
#         _, query_result = crud.read_carts_by_userId_itemId_status(db, user_id, item_id, status)


def update_cart(): 
    pass 


def delete_carts_by_userId_and_status():
    pass 

def delete_cart_by_userId_and_itemId(): 
    pass 

def update_cart_status(): 
    pass 
