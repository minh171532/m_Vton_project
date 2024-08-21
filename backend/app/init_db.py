from database import engine
from models import base 

# Create all tables
# base.Base.metadata.drop_all(bind=engine)  # use for delete all table
base.Base.metadata.create_all(bind=engine)
