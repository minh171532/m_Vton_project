from fastapi import APIRouter, Depends 
from starlette.responses import Response

from config import LOGGER
from app.utils.service_result import handle_result
from app.core import cart as core
from app.pydantic_models import CartPydantic
from app.auth import JWTBearer 


# router = APIRouter(prefix="/api/cart", tags=["/api/cart"], dependencies=[Depends(JWTBearer())])
router = APIRouter(prefix="/api/cart", tags=["/api/cart"])

@router.post("/add")
def add_to_cart(cart_pydantic: CartPydantic): 
    LOGGER.info(f"Request post add item to cart")
    response = core.add_to_cart(cart_pydantic)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)



# @router.post("/")
# def create_item(item_pydantic: ItemPydantic):
#     LOGGER.info(f"Request create user")
#     response = core.create_new_user(ItemPydantic)
#     LOGGER.info("Response: response={}".format(response))
#     return handle_result(response)

# @router.delete("/{user_id}")
# def delete_user(user_id):
#     LOGGER.info(f"Request delete user by id: {user_id}")
#     response = core.delete_user_by_id(user_id)
#     LOGGER.info("Response: response={}".format(response))
#     return handle_result(response)