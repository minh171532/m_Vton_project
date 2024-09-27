from fastapi import APIRouter, Depends , UploadFile, File
from typing import List
from starlette.responses import Response

from config import LOGGER
from app.utils.service_result import handle_result
from app.core import vton as core
from app.pydantic_models import VtonPydantic
from app.auth import JWTBearer 

# router = APIRouter(prefix="/api/vton", tags=["/api/vton"], dependencies=[Depends(JWTBearer())])
router = APIRouter(prefix="/api/vton", tags=["/api/vton"])

@router.post("/upload")
def create_vton(vton_pydantic: VtonPydantic= Depends(),
                files: List[UploadFile] = File(...)):
    LOGGER.info(f"Request update images and create inference_job")
    print(vton_pydantic)
    response = core.add_new_vton(vton_pydantic, files)
    LOGGER.info("Response: response={}".format(response))
    return handle_result(response)
    