import os
from pathlib import Path
from dotenv import load_dotenv
from setup import TIMEZONE, TIME_STR, USERNAME, EMAIL, SECRET, ALGORITHM
from setup import PYTHON_PATH, APP_PATH, STORAGE_DIR, LOG_DIR, ITEM_DIR, INFERENCE_DIR, INFERENCE_IN_DIR, INFERENCE_OUT_DIR, HUMAN_IMAGE_DIR, MASK_IMAGE_DIR         
from setup import RABBITMQ_IP, RABBITMQ_PORT, RABBITMQ_USERNAME, RABBITMQ_PASSWORD, RABBITMQ_TTL
from app.logs.timeit import timeit, async_timeit
from app.logs.log import get_log, LOG_TYPE

LOGGER = get_log(name=LOG_TYPE.LOCAL)

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class CONFIG:
    # storage dir
    STORAGE_DIR = STORAGE_DIR
    # log dir
    LOG_DIR = LOG_DIR
    # username, email 
    USERNAME = USERNAME
    EMAIL = EMAIL
    # 
    SECRET= SECRET
    ALGORITHM = ALGORITHM
    #
    ITEM_DIR = ITEM_DIR
    #
    INFERENCE_DIR = INFERENCE_DIR
    INFERENCE_IN_DIR = INFERENCE_IN_DIR
    HUMAN_IMAGE_DIR = HUMAN_IMAGE_DIR
    MASK_IMAGE_DIR = MASK_IMAGE_DIR
    INFERENCE_OUT_DIR = INFERENCE_OUT_DIR

class CONFIG_RPC:
    RABBITMQ_IP = RABBITMQ_IP
    RABBITMQ_PORT = RABBITMQ_PORT
    RABBITMQ_USERNAME = RABBITMQ_USERNAME
    RABBITMQ_PASSWORD = RABBITMQ_PASSWORD
    RABBITMQ_TTL = RABBITMQ_TTL