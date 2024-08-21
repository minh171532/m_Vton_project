import os
from pathlib import Path

from dotenv import load_dotenv

from setup import TIMEZONE, TIME_STR
from setup import PYTHON_PATH, APP_PATH, STORAGE_DIR, LOG_DIR, STATIC_DIR, SETTING_DIR
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
    # database dir
    DATABASE_DIR = os.path.join(STORAGE_DIR, "DATABASE")
    os.makedirs(DATABASE_DIR, exist_ok=True)


    # item dir
    ITEM_DIR = os.getenv('ITEM_DIR')
    ITEM_DIR = ITEM_DIR if ITEM_DIR else os.path.join(STORAGE_DIR, "ITEM")
    os.makedirs(ITEM_DIR, exist_ok=True)

    # inference dir
    INFERENCE_DIR = os.getenv('INFERENCE_DIR')
    INFERENCE_DIR = INFERENCE_DIR if INFERENCE_DIR else os.path.join(STORAGE_DIR, "INFERENCE")
    os.makedirs(INFERENCE_DIR, exist_ok=True)

    INFERENCE_IN_DIR = os.getenv('INFERENCE_IN_DIR')
    INFERENCE_IN_DIR = INFERENCE_IN_DIR if INFERENCE_IN_DIR else os.path.join(INFERENCE_DIR, "INPUT")
    os.makedirs(INFERENCE_IN_DIR, exist_ok=True)

    INFERENCE_OUT_DIR =  os.getenv('INFERENCE_OUT_DIR')
    INFERENCE_OUT_DIR = INFERENCE_OUT_DIR if INFERENCE_OUT_DIR else os.path.join(INFERENCE_DIR, "OUTPUT")
    os.makedirs(INFERENCE_OUT_DIR, exist_ok=True)