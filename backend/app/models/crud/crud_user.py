from models.user import User
from models.enums import DbOpStatus, UserRoles


def create_user(db, user: User):
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return DbOpStatus.SUCCESS, user
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)


def read_all_users(db):
    try:
        return DbOpStatus.SUCCESS, db.query(User).all()
    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)


def read_one_user(db, username):
    try:
        return DbOpStatus.SUCCESS, db.query(User).filter_by(username=username).first()

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)


def update_user(db, user_id, **kwargs):
    try:
        selected_user = db.query(User).filter_by(id=user_id).first()
        if "password" in kwargs.keys():
            selected_user.set_password(password=kwargs["password"])
        if "email" in kwargs.keys():
            selected_user.email = kwargs["email"]
        if "role" in kwargs.keys():
            selected_user.role = UserRoles(kwargs["role"])
        if "description" in kwargs.keys():
            selected_user.description = kwargs["description"]

        db.commit()

        return DbOpStatus.SUCCESS, None

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)


def delete_user(db, user_id):
    try:
        selected_user = db.query(User).filter_by(id=user_id).first()
        db.delete(selected_user)
        db.commit()
        return DbOpStatus.SUCCESS, None

    except Exception as e:
        db.rollback()  # Rollback on error
        print(f"An error occurred: {e}")
        return DbOpStatus.FAIL, str(e)
