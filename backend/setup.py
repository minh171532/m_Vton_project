__version__ = '0.1.0'

import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

PYTHON_PATH = str(Path(__file__).resolve().parent)
APP_PATH = os.path.join(PYTHON_PATH, "app")

# Set timezone
TIMEZONE = 'Asia/Bangkok' #UTC #Asia/Bangkok #Asia/Tokyo
TIME_STR = "%Y-%m-%d %H:%M:%S.%f" #[:-3]

# storage dir
STORAGE_DIR = os.getenv('STORAGE_DIR')
STORAGE_DIR = STORAGE_DIR if STORAGE_DIR else os.path.join(os.path.dirname(PYTHON_PATH), "STORAGE")
os.makedirs(STORAGE_DIR, exist_ok=True)

# log dir
LOG_DIR = os.path.join(STORAGE_DIR, "LOG")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_CONF_FILE = os.path.join(APP_PATH, "logs", "conf", "{}.conf")

# static dir
STATIC_DIR = os.path.join(APP_PATH, "static")
os.makedirs(STATIC_DIR, exist_ok=True)

# setting dir
SETTING_DIR = os.path.join(STATIC_DIR, "settings")
os.makedirs(SETTING_DIR, exist_ok=True)
