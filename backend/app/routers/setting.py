from fastapi import APIRouter
from starlette.responses import Response

from config import LOGGER
from app.core.setting import get_root_config, get_user_config
from app.utils.service_result import handle_result


router = APIRouter(prefix="/api/setting", tags=["/api/setting"])


@router.get("/root")
def get_setting_root() -> Response:
    LOGGER.info("Request:")
    response = get_root_config()
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.get("/user")
def get_setting_user() -> Response:
    LOGGER.info("Request:")
    response = get_user_config()
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)
