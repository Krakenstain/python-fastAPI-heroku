import os

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    ## Variables BD
    db_type: str = os.getenv('DB_TYPE')
    db_name: str = os.getenv('DB_NAME')
    db_user: str = os.getenv('DB_USER')
    db_pass: str = os.getenv('DB_PASS')
    db_host: str = os.getenv('DB_HOST')
    db_port: str = os.getenv('DB_PORT')

    ## REDIS
    redis_host: str = os.getenv('REDIS_HOST')
    redis_port: str = os.getenv('REDIS_PORT')
    redis_db: str = os.getenv('REDIS_DB')
    
    ## Variables JWT
    secret_key: str = os.getenv('SECRET_KEY')
    token_expire: int = os.getenv('USER_ACCESS_TOKEN_EXPIRE_MINUTES')
