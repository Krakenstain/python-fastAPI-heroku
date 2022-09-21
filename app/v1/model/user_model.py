from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, SmallInteger

from app.v1.utils.db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True) # autoincrement=True
    name = Column(String(100), nullable=False) # Nombre del usuario
    last_name = Column(String(100), nullable=False) # Apellido del usuario
    phone = Column(String(100), unique=True, nullable=False)   # Teléfono del usuario
    email = Column(String(50), unique=True, nullable=False) # Correo electrónico del usuario
    password = Column(String(256), nullable=False) # Contraseña del usuario
    status = Column(SmallInteger, default="11")  # 0:Desactivado 11:Activo 10:Eliminado
    webhook_secret = Column(String(256), nullable=False) # Token de autenticación


    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
