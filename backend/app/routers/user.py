from fastapi import APIRouter
from starlette.responses import Response

from config import LOGGER
from app.utils.service_result import handle_result
from app.core import user as core
from app.pydantic_models import UserPydantic, UserLogin


router = APIRouter(prefix="/api/user", tags=["/api/user"])


@router.get("/")
def read_users() -> Response:
    LOGGER.info("Request get users:")
    response = core.read_all_users()
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.get("/{username}")
def read_one_user(username) -> Response:
    LOGGER.info(f"Request get user by username: {username}")
    response = core.read_user_by_username(username)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)

@router.post("/login")
async def login(user: UserLogin ):
    LOGGER.info("Request: login user user={}".format(user))
    response = core.login(user)
    LOGGER.info("Response: login user result={}".format(response))
    return handle_result(response)


@router.post("/signup")
def create_user(user_pydantic: UserPydantic):
    LOGGER.info(f"Request create user")
    response = core.create_new_user(user_pydantic)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.delete("/{user_id}")
def delete_user(user_id):
    LOGGER.info(f"Request delete user by id: {user_id}")
    response = core.delete_user_by_id(user_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.put("/{user_id}")
def update_user(user_id, user_pydantic: UserPydantic):
    LOGGER.info(f"Request update user by id: {user_id}")
    response = core.update_user_by_id(user_id, user_pydantic)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)
