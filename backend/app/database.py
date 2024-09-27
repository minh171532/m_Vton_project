import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

script_path = os.path.realpath(__file__)
base_dir = os.path.dirname(os.path.dirname(script_path))
sys.path.append(base_dir)

env_path = Path('.') / '.env'
print(env_path)
load_dotenv(dotenv_path=env_path, override=True)
# load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
print(DATABASE_URL)

# Create engine
engine = create_engine(DATABASE_URL, echo=False)

# Create a configured "Session" class
Base = declarative_base()

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
