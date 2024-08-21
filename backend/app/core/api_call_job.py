import os
import socket
import traceback
from fastapi import status as http_status
from config import LOGGER
from app.utils.app_exceptions import AppExceptionCase
from app.utils.service_result import ServiceResult
from app.database import SessionLocal
from models import crud
from models.enums import DbOpStatus, JobStatus
from models.api_call_job import ApiCallJob
from backend.app.pydantic_models.item_model import ApiCallJobPydantic
from core.feature_extraction_job import delete_feature_extraction_job_by_id

db = SessionLocal()

SOCKET_SERVER_IP = os.getenv("JOB_MANAGER_IP")
SOCKET_SERVER_PORT = int(os.getenv("API_CALL_JOB_MANAGER_PORT"))


def stop_api_call(api_call_job_id: int):
    cmd_msg = f"{api_call_job_id},stop"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SOCKET_SERVER_IP, SOCKET_SERVER_PORT))
        s.sendall(str.encode(cmd_msg))
        data = s.recv(64).decode("utf-8")

    LOGGER.info(f"Received {data!r}")

    return ServiceResult({"ack_msg": data})


def delete_api_call(api_call_job_id: int):
    cmd_msg = f"{api_call_job_id},delete"
    LOGGER.info(f"Sent command: {cmd_msg}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SOCKET_SERVER_IP, SOCKET_SERVER_PORT))
        s.sendall(str.encode(cmd_msg))
        data = s.recv(64).decode("utf-8")

    LOGGER.info(f"Received {data!r}")

    return ServiceResult({"ack_msg": data})


def read_all_api_call_jobs():
    try:
        status, data = crud.read_all_api_call_jobs(db)
        if status == DbOpStatus.SUCCESS:
            return ServiceResult(data)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))


def read_api_call_jobs_by_user_id(user_id):
    try:
        status, data = crud.read_api_call_jobs_by_user_id(db, user_id)
        if status == DbOpStatus.SUCCESS:
            return ServiceResult(data)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))


def create_new_api_call_job(api_call_job_pydantic: ApiCallJobPydantic):
    try:
        api_call_job_ob = ApiCallJob(
            user_id=api_call_job_pydantic.user_id,
            job_name=api_call_job_pydantic.job_name,
            job_status=api_call_job_pydantic.job_status,
            data_dir=api_call_job_pydantic.data_dir,
            ocr_api_url=api_call_job_pydantic.ocr_api_url,
            saliency_map_api_url=api_call_job_pydantic.saliency_map_api_url
        )
        status, data = crud.create_api_call_job(db, api_call_job_ob)
        if status == DbOpStatus.SUCCESS:
            data_dict = data.__dict__
            return ServiceResult(data_dict)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        print(traceback.format_exc())
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))


def delete_api_call_job_by_id(api_call_job_id: int):
    try:
        # first, we need to stop all FE jobs that are referred to the API Call job
        _, fe_job_id_list = crud.read_feature_extraction_job_ids_by_api_call_job_id(db, api_call_job_id)
        for fe_job_id in fe_job_id_list:
            _ = delete_feature_extraction_job_by_id(fe_job_id)

        # Then emitting a message to AI core to stop => set job_status => DETELED, and delete output folder
        _ = delete_api_call(api_call_job_id)

        # Finally, delete the job in DB
        status, data = crud.delete_api_call_job(db, job_id=api_call_job_id)

        if status == DbOpStatus.SUCCESS:
            return ServiceResult(None)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        print(traceback.format_exc())
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))


def update_api_call_job_status_by_id(api_call_job_id: int, job_status: JobStatus):
    try:
        status, data = crud.update_api_call_job_status(db, job_id=api_call_job_id, job_status=job_status)
        if status == DbOpStatus.SUCCESS:
            return ServiceResult(None)
        else:
            LOGGER.error("DB Exception: {}".format(data))
            return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

    except Exception as e:
        LOGGER.error("Exception: {}".format(e))
        print(traceback.format_exc())
        return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))
