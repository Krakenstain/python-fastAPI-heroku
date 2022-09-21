# -*- coding: utf-8 -*-
from urllib.parse import urlparse

import redis
from fastapi import HTTPException, status
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.v1.utils.settings import Settings

settings = Settings()
DB_TYPE = settings.db_type
DB_NAME = settings.db_name
DB_USER = settings.db_user
DB_PASS = settings.db_pass
DB_HOST = settings.db_host
DB_PORT = settings.db_port

REDIS_URL = settings.redis_url
REDIS_URL_SSL = settings.redis_url_ssl




### REDIS ###
def get_redis():
    if REDIS_URL_SSL:
        url = urlparse(REDIS_URL)
        r = redis.Redis(host=url.hostname, port=url.port, username=url.username, password=url.password, ssl=True,
                        ssl_cert_reqs=None)
    else:
        r = redis.from_url(REDIS_URL)

    return r

redis_session = get_redis()

# El engine permite a sqlarchemy comunicarse con la bd
# https://docs.sqlalchemy.org/en/14/core/engines.html
if DB_TYPE == 'mysql':
    engine = create_engine(
        'mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}?charset=utf8'.format(
            user=DB_USER,
            passwd=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
            db=DB_NAME
        ), pool_recycle=3600, pool_pre_ping=True
    )


elif DB_TYPE == 'postgres':
    engine = create_engine(
        'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
            user=DB_USER,
            passwd=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
            db=DB_NAME
        ), pool_recycle=3600, pool_pre_ping=True
    )
elif DB_TYPE == 'sqlite':
    engine = create_engine(
        'sqlite:///{db}.sqlite3'.format(
            db=DB_NAME
        ), connect_args={"check_same_thread": False}
    )
else:
    raise Exception('Database type not supported')


# Crear la sesión es lo que permitira operar dentro de la bd
Session = sessionmaker(autocommit=True, autoflush=False, bind=engine)
session = Session()

# Dependency
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


def save_to_db(data):
    session.add(data)
    try:
        session.flush()
    except Exception as e:
        print(e.__dict__)
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="{}".format(e.__dict__)
        )

def delete_from_db(data):
    session.delete(data)
    try:
        session.flush()
    except Exception as e:
        print(e.__dict__)
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="{}".format(e.__dict__)
        )

def update_to_db():
    try:
        session.flush()
    except Exception as e:
        print(e)
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Error verifique sus datos e intente nuevamente"
        )

# se encarga de mapear la clase en la bd
Base = declarative_base()



