import os
import uuid
import json
import pytz
import platform
from datetime import datetime

import yaml
import ruamel.yaml
from easydict import EasyDict as edict

from setup import TIMEZONE



def load_yaml(config_path: str):
    """parse YAML config to EasyDict format

    Args:
        config_path (str): path to config YAML file

    Returns:
        EasyDict: config dictionary in easydict format
    """
    try:
        with open(config_path, 'r', encoding="utf-8") as f:
            config = yaml.safe_load(f)
        return edict(config)

    except Exception as err:
        print('config file cannot be read.')
        print(err)

def to_yaml(file_path, config):
    """parse EasyDict format to YAML config.

    Args:
        target_dir (str): dir to save
        config (dict): object to save

    Returns:
    """
    print("file_path", file_path)
    # file_path = os.path.join(target_dir, config["SETTING_PATH"])
    with open(file_path, "w+") as file:
        yaml = ruamel.yaml.YAML()
        yaml.indent(sequence=4, offset=2)
        yaml.dump(config, file)

def load_json(config_path):
    with open(config_path, 'r', encoding="utf-8") as config_file:
        config = json.load(config_file)
    return config

def is_platform_windows():
    return platform.system() == "Windows"
def is_platform_linux():
    return platform.system() == "Linux"

def correct_path(file_path):
    if isinstance(file_path, str):
        if is_platform_windows():
            file_path = file_path.replace('/', '\\') if '/' in file_path else file_path
        elif is_platform_linux():
            file_path = file_path.replace('\\', '/') if '\\' in file_path else file_path
    return file_path

def get_map_from_file(file):
    map = {}
    with open(correct_path(file), "r") as file:
        for line in file:
            (key, value) = line.split("=")
            map[key] = value

    return map

def uuid2str(id: uuid.UUID):
    return f'{id}'

def get_datetime_now() -> datetime:
    return datetime.now(pytz.timezone(TIMEZONE))

def get_tz():
    return pytz.timezone(TIMEZONE)
