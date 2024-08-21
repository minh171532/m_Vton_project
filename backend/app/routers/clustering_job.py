from fastapi import APIRouter
from starlette.responses import Response

from config import LOGGER
from app.utils.service_result import handle_result
from app.core import clustering_job as core
from app.pydantic_models import ClusteringJobPydantic, JobStatus


router = APIRouter(prefix="/api/clustering_job", tags=["/api/clustering_job"])


@router.post("/")
def create_clustering_job(clustering_job_pydantic: ClusteringJobPydantic):
    LOGGER.info(f"Request create clustering_job")
    response = core.create_new_clustering_job(clustering_job_pydantic)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.post("/stop/{clustering_job_id}")
def stop_clustering_job(clustering_job_id: int):
    LOGGER.info(f"Request stop {clustering_job_id}")
    response = core.stop_clustering_job(clustering_job_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.delete("/{clustering_job_id}")
def delete_clustering_job(clustering_job_id: int):
    LOGGER.info(f"Request delete clustering_job by id: {clustering_job_id}")
    response = core.delete_clustering_job_by_id(clustering_job_id)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)


@router.put("/{clustering_job_id}")
def update_clustering_job_status(clustering_job_id: int, job_status: JobStatus):
    LOGGER.info(f"Request update clustering_job by id: {clustering_job_id}")
    response = core.update_clustering_job_status_by_id(clustering_job_id, job_status)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)
