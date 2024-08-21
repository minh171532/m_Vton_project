from fastapi import APIRouter
from starlette.responses import Response

from config import LOGGER
from app.utils.service_result import handle_result
from app.core import item as core
from app.pydantic_models import ItemPydantic, Sex , ClothType  


router = APIRouter(prefix="/api/item", tags=["/api/item"])


@router.get("/")
def read_items() -> Response:
    LOGGER.info("Request get items:")
    response = core.read_items()
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)

@router.get("/{id}")
def read_one_item(id: int) -> Response:
    LOGGER.info(f"Request get item by id: {id}")
    response = core.read_item_by_id(id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)

@router.get("/sex")
def read_item_by_sex(sex: Sex) -> Response:
    LOGGER.info(f"Request get item by id: {id}")
    response = core.read_item_by_sex(sex)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)

@router.get("/sex/cloth_type")
def read_item_by_sex_cloth_type(sex:Sex, cloth_type: ClothType) -> Response:
    LOGGER.info(f"Request get item by id: {id}")
    response = core.read_item_by_sex_and_cloth_type(sex, cloth_type)
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