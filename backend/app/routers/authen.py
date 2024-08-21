from fastapi import APIRouter
from starlette.responses import Response

from config import LOGGER
from app.core.authen import check_authen
from app.utils.service_result import handle_result


router = APIRouter()


@router.post("/api/authen/{access_token}")
def authen(access_token: str) -> Response:
    LOGGER.info("Request:")
    response = check_authen(access_token)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)
