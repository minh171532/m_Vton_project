from fastapi import APIRouter
from starlette.responses import Response

from config import LOGGER
from app.utils.service_result import handle_result
from app.core import feature_extraction_job as core
from app.pydantic_models import FeatureExtractionJobPydantic, JobStatus


router = APIRouter(prefix="/api/feature_extraction_job", tags=["/api/feature_extraction_job"])


@router.post("/")
def create_feature_extraction_job(feature_extraction_job_pydantic: FeatureExtractionJobPydantic):
    LOGGER.info(f"Request create feature_extraction_job")
    response = core.create_new_feature_extraction_job(feature_extraction_job_pydantic)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.post("/stop/{feature_extraction_job_id}")
def stop_feature_extraction_job(feature_extraction_job_id: int):
    LOGGER.info(f"Request stop {feature_extraction_job_id}")
    response = core.stop_feature_extraction_job(feature_extraction_job_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.delete("/{feature_extraction_job_id}")
def delete_feature_extraction_job(feature_extraction_job_id: int):
    LOGGER.info(f"Request delete feature_extraction_job by id: {feature_extraction_job_id}")
    response = core.delete_feature_extraction_job_by_id(feature_extraction_job_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.put("/{feature_extraction_job_id}")
def update_feature_extraction_job_status(feature_extraction_job_id: int, job_status: JobStatus):
    LOGGER.info(f"Request update feature_extraction_job by id: {feature_extraction_job_id}")
    response = core.update_feature_extraction_job_status_by_id(feature_extraction_job_id, job_status)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)
