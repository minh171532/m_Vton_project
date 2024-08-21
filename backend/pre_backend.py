import os

from config import CONFIG

DATABASE_DIR = CONFIG.DATABASE_DIR
print(DATABASE_DIR)

if not os.path.isdir(DATABASE_DIR):
    os.makedirs(DATABASE_DIR)
