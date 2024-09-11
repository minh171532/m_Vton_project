from fastapi import APIRouter, Depends 
from starlette.responses import Response

from config import LOGGER
from app.utils.service_result import handle_result
from app.core import cart as core
from app.pydantic_models import CartPydantic, CartUser, CartId
from app.auth import JWTBearer 


# router = APIRouter(prefix="/api/cart", tags=["/api/cart"], dependencies=[Depends(JWTBearer())])
router = APIRouter(prefix="/api/cart", tags=["/api/cart"])

@router.post("/add")
def add_to_cart(cart_pydantic: CartPydantic): 
    LOGGER.info(f"Request post add item to cart")
    response = core.add_to_cart(cart_pydantic)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)

@router.post("/fetchAll")
def fetcAll(cart_user: CartUser): 
    LOGGER.info(f"Request post fetch all cart by userId")
    response = core.read_carts_by_userId(cart_user)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)

@router.post("/delete_all")
def deleteAll(cart_user: CartUser): 
    LOGGER.info(f"Request delete all cart by userId")
    # TODO 
    response = core.delete_carts_by_userId_and_status(cart_user)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)

@router.post("/delete")
def delete(cart_id: CartId): 
    LOGGER.info(f"Request post delete cart by userId and CartId")
    response = core.delete_cart_by_id(cart_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)

@router.post("/increment")
def increment(cart_id: CartId): 
    LOGGER.info(f"Request post UPDATE cart quantity(INCREMENT)")
    response = core.cartIncrement(cart_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)

@router.post("/decrement")
def decrement(cart_id: CartId):
    LOGGER.info(f"Request post UPDATE cart quantity(DECREMENT)")
    response = core.cartDecrement(cart_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)

# @router.post("/verifyPayment")
# def verifyPayment(): 
#     # TODO 
#     LOGGER.info(f"Request post delete cart by userId and CartId")
#     response = core.delete_cart_by_id(cart_id)
#     LOGGER.info("Response: response={}".format(response))
#     return handle_result(response)

