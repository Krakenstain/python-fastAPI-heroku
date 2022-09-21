from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi import status

from app.v1.schema import user_schema
from app.v1.schema.token_schema import Token
from app.v1.schema.user_schema import User
from app.v1.service import auth_service
from app.v1.service import user_service
from app.v1.service.auth_service import get_current_user
from app.v1.utils.db import get_db

router = APIRouter(
    prefix="/api/v1",
    tags=["Auth"]
)


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    dependencies=[Depends(get_db)],
    summary="Create a new user"
)
def create_user(
        current_user: User = Depends(get_current_user),
        user: user_schema.UserRegister = Body(...)):
    """

    ### Args
    The app can receive next fields into a JSON
    - email: A valid email
    - password: Strong password for authentication
    - name: Your name
    - last_name: Your last name
    - phone: Your phone number


    ### Returns
    - user: User info
    """
    return user_service.create_user(user)


@router.post(
    "/login",
    response_model=Token,
    status_code=status.HTTP_200_OK,
    summary="Login user"
)
def login_for_access_token(user: user_schema.UserLogin = Body(...)):
    """

    ### Args
    The app can recive next fields into a JSON
    - email: Your username or email
    - password: Your password

    ### Returns
    - access token and token type
    """

    access_token = auth_service.generate_token(user.email, user.password)
    return Token(access_token=access_token, token_type="bearer")

