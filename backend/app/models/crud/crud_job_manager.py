from models import crud
from models.enums import DbOpStatus


LIST_FN = [
    crud.read_all_api_call_jobs,
    crud.read_all_feature_extraction_jobs,
    crud.read_all_clustering_jobs,
    crud.read_all_inference_jobs,
]

LIST_FN_BY_USER_ID = [
    crud.read_api_call_jobs_by_user_id,
    crud.read_feature_extraction_jobs_by_user_id,
    crud.read_clustering_jobs_by_user_id,
    crud.read_inference_jobs_by_user_id,
]


def read_all_jobs(db):
    total_res = []

    for fn in LIST_FN:
        status, data = fn(db)
        if status == DbOpStatus.SUCCESS:
            total_res.extend(data)
        else:
            return DbOpStatus.FAIL, str(data)

    return DbOpStatus.SUCCESS, total_res


def read_all_jobs_by_user_id(db, user_id):
    total_res = []

    for fn in LIST_FN_BY_USER_ID:
        status, data = fn(db, user_id)
        if status == DbOpStatus.SUCCESS:
            total_res.extend(data)
        else:
            return DbOpStatus.FAIL, str(data)

    return DbOpStatus.SUCCESS, total_res
