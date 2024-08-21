from database import SessionLocal
from models import crud
from models import *
from models.enums import *

if __name__ == "__main__":
    db = SessionLocal()
    # ================================
    # username = "minhpb2"
    # email = "minh_ac@gmail.com"

    # print("Test User")
    # # test read and delete function
    # ret_code, user_ob = crud.read_one_user(db, username)
    # print(ret_code)
    # if ret_code == DbOpStatus.SUCCESS and user_ob is not None:
    #     ret_code = crud.delete_user(db=db, user_id=user_ob.id)
    #     print(ret_code)

    # # test create function
    # # try to remove user if it existed
    # user = User(
    #     username=username,
    #     email=email,
    #     role=UserRoles.ADMIN
    # )
    # user.set_password(password="helloworld")

    # ret_code, created_user = crud.create_user(db=db, user=user)
    # print(ret_code, created_user.username)

    # # test update function
    # new_password = "Abcd1234"
    # update_info = {
    #     "password": new_password,
    #     "desciption": "Key Developper"
    # }
    # ret_code = crud.update_user(db, created_user.id, **update_info)
    # print(ret_code)

    # # ==============================
    # print("Test item")
    # item = Item(
    #     tag="sirt",
    #     image_dir="abcd",
    #     mask_dir="bcda",
    # )
    # ret_code, created_item = crud.create_item(db=db, item=item)
    # print(ret_code)

    # # =============================
    # user_item = UserItem(
    #     user_id=created_user.id,
    #     item_id=created_item.id,
    #     item_quantity = 0,
    #     status = JobStatus.WAITING,
    #     vton_mode =VtonMode.UP
    # )
    # ret_code, create_user_item = crud.create_user_item(db=db, userItem=user_item)
    # print(ret_code)
    ret_code, all_user_item = crud.read_all_users_items(db=db)
    print(ret_code)
    for _item in all_user_item:
        print(_item)
