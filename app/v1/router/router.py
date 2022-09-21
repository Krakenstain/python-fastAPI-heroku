from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body

from app.v1.schema.user_schema import User
from app.v1.service.auth_service import get_current_user
from app.v1.utils.db import get_db

router = APIRouter(
    prefix="",
    tags=["TEST ROUTER"]
)


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get(
    "/hello",
    status_code=status.HTTP_200_OK,
    summary="Hello {name}",
    dependencies=[Depends(get_db)]
)
async def say_hello(
        current_user: User = Depends(get_current_user)
):

    return {"message": f"Hello {current_user.name}"}