# import traceback
# from fastapi import status as http_status
# from config import LOGGER
# from app.utils.app_exceptions import AppExceptionCase
# from app.utils.service_result import ServiceResult
# from app.database import SessionLocal
# from models import crud
# from models.enums import DbOpStatus, JobStatus
# from backend.app.pydantic_models.item_model import ApiCallJobPydantic

# db = SessionLocal()


# def read_all_jobs():
#     try:
#         status, data = crud.read_all_jobs(db)
#         if status == DbOpStatus.SUCCESS:
#             return ServiceResult(data)
#         else:
#             LOGGER.error("DB Exception: {}".format(data))
#             return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

#     except Exception as e:
#         LOGGER.error("Exception: {}".format(e))
#         return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))


# def read_all_jobs_by_user_id(user_id):
#     try:
#         status, data = crud.read_all_jobs_by_user_id(db, user_id)
#         if status == DbOpStatus.SUCCESS:
#             return ServiceResult(data)
#         else:
#             LOGGER.error("DB Exception: {}".format(data))
#             return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=data))

#     except Exception as e:
#         LOGGER.error("Exception: {}".format(e))
#         return ServiceResult(AppExceptionCase(status_code=http_status.HTTP_500_INTERNAL_SERVER_ERROR, context=str(e)))
