from fastapi import APIRouter
from starlette.responses import Response

from config import LOGGER
from app.utils.service_result import handle_result
from app.core import job_manager as core


router = APIRouter(prefix="/api/job_manager", tags=["/api/job_manager"])


@router.get("/")
def read_all_jobs() -> Response:
    LOGGER.info("Request get all jobs:")
    response = core.read_all_jobs()
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.get("/{user_id}")
def read_all_jobs_by_user_id(user_id: str) -> Response:
    LOGGER.info(f"Request get all jobs by user_id: {user_id}")
    response = core.read_all_jobs_by_user_id(user_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)
