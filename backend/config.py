import os
from pathlib import Path
from dotenv import load_dotenv
from setup import TIMEZONE, TIME_STR, USERNAME, EMAIL
from setup import PYTHON_PATH, APP_PATH, STORAGE_DIR, LOG_DIR, DATABASE_DIR, ITEM_DIR, INFERENCE_DIR, INFERENCE_IN_DIR, INFERENCE_OUT_DIR           
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
    DATABASE_DIR = DATABASE_DIR
    #
    ITEM_DIR = ITEM_DIR
    #
    INFERENCE_DIR = INFERENCE_DIR
    INFERENCE_IN_DIR = INFERENCE_IN_DIR
    INFERENCE_OUT_DIR = INFERENCE_OUT_DIR