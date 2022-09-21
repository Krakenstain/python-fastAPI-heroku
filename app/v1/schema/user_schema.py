from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserBase(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Roberto"
    )
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        example="Perez Perez"
    )
    phone: str = Field(
        ...,
        min_length=3,
        max_length=100,
        example="+56912345678"
    )
    email: EmailStr = Field(
        ...,
        example="myemail@dominio.com"
    )



class User(UserBase):
    id: int = Field(
        ...,
        example="5"
    )

class UserRegister(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="stronGpass123*"
    )

class UserLogin(BaseModel):
    email: EmailStr = Field(
        ...,
        example="myemail@dominio.com"
    )
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
        example="stronGpass123*"
    )


