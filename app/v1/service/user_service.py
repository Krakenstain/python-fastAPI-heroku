from secrets import token_hex

from fastapi import HTTPException, status

from app.v1.model.user_model import User as UserModel
from app.v1.schema import user_schema
from app.v1.service.auth_service import get_password_hash
from app.v1.utils.db import session


def create_user(user: user_schema.UserRegister):
    get_user = session.query(UserModel).filter(
        (UserModel.email == user.email) ).first()

    if get_user:
        msg = "Email already registered"
        if get_user.email == user.email:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

    webhook_secret = token_hex(15)

    db_user = UserModel(
        email=user.email,
        name=user.name,
        last_name=user.last_name,
        phone=user.phone,
        password=get_password_hash(user.password),
        webhook_secret=webhook_secret,
    )

    session.add(db_user)
    try:
        session.flush()
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error verifique sus datos e intente nuevamente"
        )

    return user_schema.User(
        id=db_user.id,
        email=db_user.email,
        name=user.name,
        last_name=user.last_name,
        phone=user.phone
    )


def get_user(user_id: int):
    get_user = session.query(UserModel).filter((UserModel.id == user_id)).first()

    if get_user is None:
        msg = "User not found"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )


    return user_schema.User(
        id=get_user.id,
        email=get_user.email,
        name=get_user.name,
        last_name=get_user.last_name,
        phone=get_user.phone,
    )
