from database import engine
from models import base 

# Create all tables
base.Base.metadata.drop_all(bind=engine)  # use for delete all table

base.Base.metadata.create_all(bind=engine)

# ===============
import os 
import glob
import uuid 
from database import SessionLocal
from models import crud
from models import * 
from models.enums import *
import sys 
sys.path.append("../")
from config import CONFIG

db = SessionLocal()
# ===============================
# add admin user into users table 
# ===============================
ret_code, user_ob = crud.read_one_user(db, CONFIG.USERNAME)
if ret_code == DbOpStatus.SUCCESS and user_ob is not None:
    ret_code = crud.delete_user(db=db, user_id=user_ob.id)

user = User(
    username=CONFIG.USERNAME,
    email=CONFIG.EMAIL,
    firstName="abc",
    lastName="abc",

    # role=UserRoles.ADMIN
)
user.set_password(password="helloworld")
ret_code, created_user = crud.create_user(db=db, user=user)

# ============================
# Add items into item database 
# ============================
items_path = CONFIG.ITEM_DIR 
sexFolders = os.listdir(items_path)
for sexFolder in sexFolders: 
    sexFolder_dir = os.path.join(items_path, sexFolder)
    clothTypes = os.listdir(sexFolder_dir)
    for clothType in clothTypes: 
        clothType_dir = os.path.join(sexFolder_dir, clothType)
        item_imgs = os.listdir(clothType_dir)
        
        for item_img in item_imgs:             
            item_img_dir = os.path.join(clothType_dir, item_img)
            imgs = glob.glob(os.path.join(item_img_dir, '*', "*.png")) \
                    + glob.glob(os.path.join(item_img_dir, '*', "*.jpg")) \
                    + glob.glob(os.path.join(item_img_dir, '*', "*.jpeg"))

            if len (imgs) < 1: 
                continue
            item = Item(
                sex=sexFolder,
                category=clothType,
                title="title",
                description="description",
                price=400000,
                image_folder_dir=os.path.join(sexFolder, clothType, item_img),
            )
            ret_code, created_item = crud.create_item(db=db, item=item)
            print("add item into database", ret_code)
            # ============================
            # Add item_store into item database 
            # ============================
            colors = os.listdir(item_img_dir)
            for color in colors: 
                item_store = ItemStore(
                    image_folder_dir=os.path.join(sexFolder, clothType, item_img),
                    color=color,
                    s_no=10, 
                    m_no=10,
                    l_no=10,
                    xl_no=10,
                    xxl_no=10
                )
                ret_code, created_item_store = crud.create_item_store(db=db, item_store=item_store )
                print("add item store into database", ret_code)
                print("item_store", created_item_store.__dict__)

    # # create new cart, bill 
    # # created_user = created_user.__dict__ 
    # cart = Cart(
    #     item_id=created_item.id,
    #     user_id=created_user.id,
    #     bill_id="temp",
    #     quantity= 1,
    #     color="green",
    #     size=Size.M, 
    #     status=CartStatus.CHECKOUT
    # )

    # _, cart_= crud.create_cart(db=db, cart=cart)

    # print("cart >>>> ", cart.__dict__) 
    # # create new_bill 
    
    # bill = Bill(
    #     id = str(uuid.uuid4()),
    #     name = "temp",
    #     phone_number = "temp",
    #     location="temp",
    #     total_price = 20
    # )
    # _, bill_ = crud.create_bill(db=db, bill=bill)
    # print(bill.__dict__)
