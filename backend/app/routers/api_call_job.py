from fastapi import APIRouter
from starlette.responses import Response

from config import LOGGER
from app.utils.service_result import handle_result
from app.core import api_call_job as core
from app.pydantic_models import ApiCallJobPydantic, JobStatus


router = APIRouter(prefix="/api/api_call_job", tags=["/api/api_call_job"])


@router.post("/")
def create_api_call_job(api_call_job_pydantic: ApiCallJobPydantic):
    LOGGER.info(f"Request create api_call_job")
    response = core.create_new_api_call_job(api_call_job_pydantic)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.post("/stop/{api_call_job_id}")
def stop_api_call_job(api_call_job_id: int):
    LOGGER.info(f"Request stop {api_call_job_id}")
    response = core.stop_api_call(api_call_job_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.delete("/{api_call_job_id}")
def delete_api_call_job(api_call_job_id: int):
    LOGGER.info(f"Request delete api_call_job by id: {api_call_job_id}")
    response = core.delete_api_call_job_by_id(api_call_job_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.put("/{api_call_job_id}")
def update_api_call_job_status(api_call_job_id: int, job_status: JobStatus):
    LOGGER.info(f"Request update api_call_job by id: {api_call_job_id}")
    response = core.update_api_call_job_status_by_id(api_call_job_id, job_status)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)
